import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    """ retrieving keys and adding them to the project
    from the .env file through their key names
    """

    # FETCH DATASET
    MODULES_TO_DATASETS_PATH = os.getenv("MODULES_TO_DATASETS_PATH")

    DATA_EU_AIR_F1_1 = os.getenv("DATA_EU_AIR_F1_1")
    DATA_EU_AIR_F1_2 = os.getenv("DATA_EU_AIR_F1_2")
    DATA_EU_AIR_F1_3 = os.getenv("DATA_EU_AIR_F1_3")
    DATA_EU_AIR_F1_4 = os.getenv("DATA_EU_AIR_F1_4")

    CO2_CO2_Factor_Equivalence_20_Years = 1

    # CO2 Factor Equivalence on a 20 years base
    NMVOC_CO2_Factor_Equivalence_20_Years = 5.83  # consensus non défini, donc à vérifier
    NOX_CO2_Factor_Equivalence_20_Years = 0
    SOX_CO2_Factor_Equivalence_20_Years = 0
    CO_CO2_Factor_Equivalence_20_Years = 0
    CH4_CO2_Factor_Equivalence_20_Years = 0
    Hg_CO2_Factor_Equivalence_20_Years = 0
    PM10_CO2_Factor_Equivalence_20_Years = 0
    N2O_CO2_Factor_Equivalence_20_Years = 0
    HCFCs_CO2_Factor_Equivalence_20_Years = 0
    Cr_CO2_Factor_Equivalence_20_Years = 0
    Zn_CO2_Factor_Equivalence_20_Years = 0
    Cu_CO2_Factor_Equivalence_20_Years = 0
    Pb_CO2_Factor_Equivalence_20_Years = 0
    NH3_CO2_Factor_Equivalence_20_Years = 0
    Benzene_CO2_Factor_Equivalence_20_Years = 0
    DCM_CO2_Factor_Equivalence_20_Years = 0
    Cd_CO2_Factor_Equivalence_20_Years = 0
    Ni_CO2_Factor_Equivalence_20_Years = 0
    Teq_CO2_Factor_Equivalence_20_Years = 0
    HFCS_CO2_Factor_Equivalence_20_Years = 0
    HCl_CO2_Factor_Equivalence_20_Years = 0
    As_CO2_Factor_Equivalence_20_Years = 0
    HF_CO2_Factor_Equivalence_20_Years = 0
    CO2_Excluding_Biomass_CO2_Factor_Equivalence_20_Years = 0
    CFCs_CO2_Factor_Equivalence_20_Years = 0

    # CO2 Factor Equivalence on a 100 years base
    NMVOC_CO2_Factor_Equivalence_100_Years = 2.36  # consensus non défini, donc à vérifier
    NOX_CO2_Factor_Equivalence_100_Years = 0
    SOX_CO2_Factor_Equivalence_100_Years = 0
    CO_CO2_Factor_Equivalence_100_Years = 0
    CH4_CO2_Factor_Equivalence_100_Years = 0
    Hg_CO2_Factor_Equivalence_100_Years = 0
    PM10_CO2_Factor_Equivalence_100_Years = 0
    N2O_CO2_Factor_Equivalence_100_Years = 0
    HCFCs_CO2_Factor_Equivalence_100_Years = 0
    Cr_CO2_Factor_Equivalence_100_Years = 0
    Zn_CO2_Factor_Equivalence_100_Years = 0
    Cu_CO2_Factor_Equivalence_100_Years = 0
    Pb_CO2_Factor_Equivalence_100_Years = 0
    NH3_CO2_Factor_Equivalence_100_Years = 0
    Benzene_CO2_Factor_Equivalence_100_Years = 0
    DCM_CO2_Factor_Equivalence_100_Years = 0
    Cd_CO2_Factor_Equivalence_100_Years = 0
    Ni_CO2_Factor_Equivalence_100_Years = 0
    Teq_CO2_Factor_Equivalence_100_Years = 0
    HFCS_CO2_Factor_Equivalence_100_Years = 0
    HCl_CO2_Factor_Equivalence_100_Years = 0
    As_CO2_Factor_Equivalence_100_Years = 0
    HF_CO2_Factor_Equivalence_100_Years = 0
    CO2_Excluding_Biomass_CO2_Factor_Equivalence_100_Years = 0
    CFCs_CO2_Factor_Equivalence_100_Years = 0

settings = Settings()
