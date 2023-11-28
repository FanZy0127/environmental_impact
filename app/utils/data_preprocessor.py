import pandas as pd

class DataPreprocessor:
    @staticmethod
    def __pollutant_features(d_frame: pd.DataFrame) -> pd.DataFrame:
        df_pivoted = d_frame\
            .pivot_table(
                index=["FacilityInspireID", "reportingYear"],
                columns="pollutant",
                values="emissions",
                aggfunc="sum")\
            .reset_index()

        df_pivoted.iloc[:, 2:] = df_pivoted.iloc[:, 2:].fillna(0)

        return df_pivoted
    
    @staticmethod
    def __df_with_pollutant_features(df_unique: pd.DataFrame, df_pollutant: pd.DataFrame) -> pd.DataFrame:
        return pd.merge(df_unique, df_pollutant, on=["FacilityInspireID", "reportingYear"], how="left")

    @staticmethod
    def __drop_columns(d_frame: pd.DataFrame) -> pd.DataFrame:
        columns_to_drop = [
            "countryName", "facilityName", "EPRTRSectorCode", "EPRTRAnnexIMainActivityCode", 
            "facilityNameConfidentialityReason", "Longitude", "Latitude", 
            "addressConfidentialityReason", "City", "targetRelease", 
            "releasesConfidentialityReason", "EPRTRAnnexIMainActivityLabel", "CONFIDENTIAL"
        ]

        return d_frame.drop(columns=columns_to_drop)

    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        data_copy = data.copy()

        df_unique = data_copy.drop_duplicates(subset=["FacilityInspireID", "reportingYear"])
        df_unique = df_unique.drop(columns=["pollutant", "emissions"])

        df_pollutant = self.__pollutant_features(data_copy)
        df_final = self.__df_with_pollutant_features(df_unique, df_pollutant)
        df_final = df_final[df_final["releasesConfidentialityReason"].isna()]
        df_final = self.__drop_columns(df_final)
        df_final = df_final[~df_final["eprtrSectorName"].isna()]

        return df_final