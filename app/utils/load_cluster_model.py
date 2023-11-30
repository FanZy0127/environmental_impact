from joblib import load
from fastapi import HTTPException
from app.config.settings import settings

def load_cluster_model(sector_name: str):
    model_path = settings.models_path + settings.models_kmeans_names + sector_name + ".joblib"
    try:
        return load(model_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Cluster model for sector '{sector_name}' not found.")
