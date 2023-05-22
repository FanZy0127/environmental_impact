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
    DATA_EU_AIR_F1_1 = os.getenv("DATA_EU_AIR_F1_1")
    DATA_EU_AIR_F1_2 = os.getenv("DATA_EU_AIR_F1_2")
    DATA_EU_AIR_F1_3 = os.getenv("DATA_EU_AIR_F1_3")
    DATA_EU_AIR_F1_4 = os.getenv("DATA_EU_AIR_F1_4")
    

settings = Settings()
