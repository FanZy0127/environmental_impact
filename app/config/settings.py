from pydantic import BaseSettings

class Settings(BaseSettings):
    files_path: str
    air_dataset: str
    models_path: str
    models_kmeans_names: str
    models_random_name: str

    class Config:
        env_file = ".env"

settings = Settings()