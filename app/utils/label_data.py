import pandas as pd

class LabelData:
    def __init__(self):
        self.grades = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.quantiles = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 0.99]

    def calculate_emission_quantiles(self, df: pd.DataFrame):
        self.group_by_sector_pollutant = df.groupby(["eprtrSectorName", "pollutant"])["emissions"]\
            .quantile(q=self.quantiles)\
            .reset_index()\
            .rename(columns={"level_2": "Quantile", "emissions": "EmissionsQuantile"})

    def get_category(self, sector: str, pollutant: str, emission: float) -> float:
        subset = self.group_by_sector_pollutant[
            (self.group_by_sector_pollutant.eprtrSectorName == sector) &
            (self.group_by_sector_pollutant.pollutant == pollutant) &
            (self.group_by_sector_pollutant.EmissionsQuantile < emission)
        ]["Quantile"]

        return subset.iloc[-1] if len(subset) > 0 else 0.0

    def map_quantile_to_grade(self, quantile):
        if 0 <= quantile <= 1:
            index = int(quantile * 8) - 1 if quantile > 0 else 0
            return self.grades[index]
        return "Unknown"

    def process(self, df: pd.DataFrame) -> pd.DataFrame:
        df_copy = df.copy()
        self.calculate_emission_quantiles(df_copy)

        df_copy["Quantile"] = df_copy.apply(
            lambda x: self.get_category(
                x["eprtrSectorName"],
                x["pollutant"],
                x["emissions"]
            ),
            axis=1
        )

        df_copy["Grade"] = df_copy["Quantile"].apply(self.map_quantile_to_grade)

        return df_copy