import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1_4 = pd.read_csv("./datasets/european_companies/CSV/F1_4_Detailed releases at facility level with E-PRTR Sector and Annex I Activity detail into Air.csv", low_memory=False)
# print(df1_4.info())
# print(df1_4.columns)

df_pivoted = df1_4.pivot_table(index=['FacilityInspireID', 'reportingYear'],
                                columns='pollutant',
                                values='emissions',
                                aggfunc='sum').reset_index()

df_pivoted.reset_index(inplace=True)
df_pivoted.iloc[:, 3:] = df_pivoted.iloc[:, 3:].fillna(0)

df_unique = df1_4.drop_duplicates(subset=['FacilityInspireID', 'reportingYear']).drop(columns=['pollutant', 'emissions'])

df_final = pd.merge(df_unique, df_pivoted, on=['FacilityInspireID', 'reportingYear'], how='left')
df_final = df_final.drop(columns=['index'])
# print(df_final.iloc[0,15:])
# print(df_final.info())
# print(df_final.head())
print(df_final.iloc[:, 15:].corr())
sns.heatmap(df_final.iloc[:, 15:], annot=True, cmap='coolwarm')
plt.savefig("seaborn_plot.png")