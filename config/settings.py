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

    GWP = {
        '1,2-dichloroethane (DCE-1,2)' : 0,
        'Non-methane volatile organic compounds (NMVOC)' : 0,
        'Carbon dioxide (CO2)' : 1, 
        'Nitrogen oxides (NOX)' : 0,
        'Sulphur oxides (SOX)' : 0, 
        'Zinc and compounds (as Zn)' : 0,
        'Carbon monoxide (CO)' : 0, 
        'Methane (CH4)' : 25,
        'Mercury and compounds (as Hg)' : 0, 
        'Hydrogen cyanide (HCN)' : 0,
        'Particulate matter (PM10)' : 0, 
        'Nitrous oxide (N2O)' : 298,
        'Hydrochlorofluorocarbons (HCFCs)' : 0,
        'Chromium and compounds (as Cr)' : 0, 
        'Copper and compounds (as Cu)' : 0,
        'Lead and compounds (as Pb)' : 0,
        'Chlorine and inorganic compounds (as HCl)' : 0, 
        'Ammonia (NH3)' : 0,
        'Benzene' : 0, 
        'Polycyclic aromatic hydrocarbons (PAHs)' : 0,
        'Dichloromethane (DCM)' : 0, 
        'Cadmium and compounds (as Cd)' : 0,
        'Nickel and compounds (as Ni)' : 0,
        'PCDD + PCDF (dioxins + furans) (as Teq)' : 0,
        'Hydro-fluorocarbons (HFCS)' : 2448,  # Moyenne de 19 gaz
        'Fluorine and inorganic compounds (as HF)' : 0, 
        'Naphthalene' : 0,
        'Arsenic and compounds (as As)' : 0, 
        'Sulphur hexafluoride (SF6)' : 22800,
        'Trichloroethylene (TRI)' : 0, 
        'Perfluorocarbons (PFCs)' : 10098,  # Moyenne de 9 gaz
        'Anthracene' : 0,
        'Benzo(g,h,i)perylene' : 0, 
        'Polychlorinated biphenyls (PCBs)' : 0,
        'Chlorofluorocarbons (CFCs)' : 6226,  # 2021
        'Di-(2-ethyl hexyl) phthalate (DEHP)' : 0, 
        'Vinyl chloride' : 0,
        'Tetrachloroethylene' : 0, 
        'Halons' : 0, 
        'Tetrachloromethane (TCM)' : 0,
        'Trichloromethane' : 0, 
        'Ethylene oxide' : 0,
        'Carbon dioxide (CO2) excluding biomass' : 1,
        'Total organic carbon(as total C or COD/3) (TOC)' : 0,
        '1,1,1-trichloroethane (TCE-1,1,1)' : 0,
        '1,1,2,2-tetrachloroethane (TETRACHLOROETHANE-1,1,2,2)' : 0,
        'Trichlorobenzenes (TCB)' : 0, 
        'Phenols (as total C)' : 0,
        'Fluorides (as total F)' : 0, 
        'Fluoranthene' : 0
    }

settings = Settings()
