import pandas as pd

df1_4 = pd.read_csv("./datasets/european_companies/CSV/F1_4_Detailed releases at facility level with E-PRTR Sector and Annex I Activity detail into Air.csv", low_memory=False)
# print(df1_4.head())
print(df1_4.info())
print(df1_4.columns)
# print(df1_4.pollutant.value_counts())
# print(df1_4.targetRelease.value_counts())
# print(df1_4.emissions.value_counts())


df_pivoted = df1_4.pivot_table(index=['FacilityInspireID', 'reportingYear'],
                                columns='pollutant',
                                values='emissions',
                                aggfunc='sum').reset_index()

df_pivoted.reset_index(inplace=True)

df_unique = df1_4.drop_duplicates(subset=['FacilityInspireID', 'reportingYear']).drop(columns=['pollutant', 'emissions'])

# Now df_pivoted has pollutants as columns (features) and emissions as values
# df_final = df_unique.join(df_pivoted, on=['FacilityInspireID', 'reportingYear'])
df_final = pd.merge(df_unique, df_pivoted, on=['FacilityInspireID', 'reportingYear'], how='left')
df_final.drop(columns=['index'])
print(df_final.info())
print(df_final.head())
print(df_final.loc[220, :].to_string())
