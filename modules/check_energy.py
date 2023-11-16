import pandas as pd
import sys
sys.path.append('./')
from config.settings import settings

DATASETS_BASE = settings.MODULES_TO_DATASETS_PATH

df = pd.read_csv("./datasets/european_companies/CSV/F5_2_Detailed emissions and energy input from LCP.csv")
print(df.info())
print("-----------------------------------")
print(df.columns)
print("-----------------------------------")
print("FeatureType: ", df.featureType.unique())
print("-----------------------------------")
print("Feature: ", df.feature.unique())
print("-----------------------------------")
print("LCPInspireID: ", df.LCPInspireID.value_counts())
print("-----------------------------------")
print(df.head())

print("----------------AIR-------------------")

df1_4 = pd.read_csv("./datasets/european_companies/CSV/F1_4_Detailed releases at facility level with E-PRTR Sector and Annex I Activity detail into Air.csv", low_memory=False)
print(df1_4.head())
print(df1_4.info())
print(df1_4.columns)

print("----------------INFO-------------------")

df6_1 = pd.read_csv("./datasets/european_companies/CSV/F6_1_Total Information on Installations.csv", low_memory=False)
print(df6_1.head())
print(df6_1.info())
print(df6_1.columns)
print(df6_1.featureType.value_counts())

print("----------------AIR 1-------------------")

df1_1 = pd.read_csv("./datasets/european_companies/CSV/F1_1_Total Releases at National Level into Air.csv", low_memory=False)
print(df1_1.head())
print(df1_1.info())
print(df1_1.columns)

print("----------------TRANSFER 1-------------------")

df3_1 = pd.read_csv("./datasets/european_companies/CSV/F3_1_Total pollutant transfer.csv", low_memory=False)
print(df3_1.head())
print(df3_1.info())
print(df3_1.columns)

print("----------------TRANSFER 2-------------------")

df3_2 = pd.read_csv("./datasets/european_companies/CSV/F3_2_Detailed pollutant transfer at facility level with E-PRTR Sector and Annex I Activity.csv", low_memory=False)
print(df3_2.head())
print(df3_2.info())
print(df3_2.columns)

print("-----------------COMPARAISON-------------------")
df1_4.FacilityInspireID = df1_4.FacilityInspireID.str.replace('.Facility', '', regex=False)
df.LCPInspireID = df.LCPInspireID.str.replace('.PART', '', regex=False)

common_values = pd.Series(list(set(df1_4['FacilityInspireID']).intersection(set(df['LCPInspireID']))))

# Number of unique common values
num_common_unique_values = common_values.nunique()
print(num_common_unique_values, common_values.tolist())