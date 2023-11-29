# import pandas as pd
# import numpy as np
# from fastapi import APIRouter, Depends, HTTPException
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# from joblib import dump
# from app.schemas.cluster_config import ClusterConfig
# from app.utils.get_cluster_config import get_cluster_config
# from app.utils.label_data import LabelData
# from app.config.settings import settings

# router = APIRouter()

# @router.post(
#     "/train_classification",
#     description="Entraine le modèle de classification avec un nouveau dataset.",
# )
# def train_classification(
#     config: ClusterConfig = Depends(get_cluster_config),
#     labels: LabelData = Depends(LabelData)
# ):
#     try:
#         df = pd.read_csv(config.dataset_path, low_memory=False)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

#     df_labeled = labels.process(df)

#     # Agrégation et préparation des données
#     df_agg_per_FacilityInspireID_per_year = df_labeled.groupby(
#         ["FacilityInspireID", "reportingYear"]
#     )["Grade"].agg(
#         lambda x: x.mode()[0] if not x.mode().empty else np.nan
#     ).reset_index()

#     X = df_agg_per_FacilityInspireID_per_year.drop(columns=["Grade", "FacilityInspireID"])
#     y = df_agg_per_FacilityInspireID_per_year["Grade"]

#     # Séparation des données en ensemble d'entraînement et de test
#     X_train, X_test, y_train, y_test = train_test_split(
#         X, y, test_size=0.2, random_state=42
#     )

#     classifier = RandomForestClassifier(random_state=42)
#     classifier.fit(X_train, y_train)

#     predictions = classifier.predict(X_test)
#     score = accuracy_score(y_test, predictions)

#     model_filename = settings.models_path + settings.models_random_name + ".joblib"
#     dump(classifier, model_filename)

#     return {"message": "Model trained successfully", "result": score}