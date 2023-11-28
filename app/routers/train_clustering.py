import pandas as pd
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.cluster_config import ClusterConfig
from app.utils.data_preprocessor import DataPreprocessor
from app.utils.cluster_service import ClusterService
from app.utils.get_cluster_config import get_cluster_config

router = APIRouter()

@router.post(
    "/train_clustering",
    description="Entraine le modèle de clustering KMEANS avec un nouveau dataset.",
)
async def train_clustering(
    config: ClusterConfig = Depends(get_cluster_config),
    preprocessor: DataPreprocessor = Depends(DataPreprocessor)
):
    try:
        df = pd.read_csv(config.dataset_path, low_memory=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    processed_data = preprocessor.preprocess(df)

    service = ClusterService(param_grid=config.parameter_grid)
    clusters_df, clusters_info = service.cluster_data(processed_data, sector_col="eprtrSectorName")

    return {"message": "Model trained successfully", "result": str(clusters_info)}