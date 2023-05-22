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
    DATASETS_PATH = os.getenv("DATASETS_PATH")
    

settings = Settings()