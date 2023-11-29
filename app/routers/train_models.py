import pandas as pd
import numpy as np
from fastapi import APIRouter, HTTPException, Depends
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from joblib import dump
from app.config.settings import settings
from app.schemas.cluster_config import ClusterConfig
from app.utils.data_preprocessor import DataPreprocessor
from app.utils.cluster_service import ClusterService
from app.utils.get_cluster_config import get_cluster_config
from app.utils.label_data import LabelData


router = APIRouter()

@router.post(
    "/train_models",
    description="Entraine le modèle de clustering KMEANS et de classification RandomForest avec un nouveau dataset.",
)
async def train_models(
    config: ClusterConfig = Depends(get_cluster_config),
    preprocessor: DataPreprocessor = Depends(DataPreprocessor),
    labels: LabelData = Depends(LabelData)
):
    try:
        df = pd.read_csv(config.dataset_path, low_memory=False)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Cluster
    processed_data = preprocessor.preprocess(df)

    service = ClusterService(param_grid=config.parameter_grid)
    clusters_df, clusters_info = service.cluster_data(processed_data, sector_col="eprtrSectorName")

    # Classification
    df_labeled = labels.process(df)

    df_agg_per_FacilityInspireID_per_year = df_labeled.groupby(
        ["FacilityInspireID", "reportingYear"]
    )["Grade"].agg(
        lambda x: x.mode()[0] if not x.mode().empty else np.nan
    ).reset_index()

    merged_df = pd.merge(df_agg_per_FacilityInspireID_per_year, clusters_df, 
                         on=["FacilityInspireID", "reportingYear"], how="left")
    merged_df = merged_df.dropna()

    encoder = LabelEncoder()
    merged_df["sectorCluster"] = encoder.fit_transform(merged_df["sectorCluster"])

    # Préparation des features et des labels pour la classification
    X = merged_df.drop(columns=["Grade", "FacilityInspireID", "reportingYear", "cluster", "eprtrSectorName"])
    y = merged_df["Grade"]

    # Séparation des données en ensemble d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # pca = PCA(n_components=0.95) 
    # X_train_pca = pca.fit_transform(X_train)
    # X_test_pca = pca.transform(X_test)

    classifier = RandomForestClassifier(random_state=42)
    classifier.fit(X_train, y_train)

    predictions = classifier.predict(X_test)
    score = accuracy_score(y_test, predictions)

    model_filename = settings.models_path + settings.models_random_name + ".joblib"
    dump(classifier, model_filename)

    return {"message": "Model trained successfully", "result_cluster": str(clusters_info), "result_classification": score}