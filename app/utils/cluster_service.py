import pandas as pd
from typing import Any, Dict, List
from joblib import dump
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans, DBSCAN, OPTICS
from sklearn.metrics import silhouette_score
from sklearn.model_selection import ParameterGrid
from app.config.settings import settings

class ClusterService:
    def __init__(self, param_grid: Dict[str, List[Any]]):
        self.param_grid = param_grid

    def scale_features(self, df: pd.DataFrame, pollutant_cols: List[str]) -> pd.DataFrame:
        scaler = MinMaxScaler()
        return scaler.fit_transform(df[pollutant_cols]), scaler
    
    def find_optimal_params(self, data: pd.DataFrame) -> Dict[str, Any]:
        best_score = float("-inf")
        best_params = None

        for params in ParameterGrid(self.param_grid):
            model = KMeans(**params)
            model.fit(data)
            score = silhouette_score(data, model.labels_)

            if score > best_score:
                best_score = score
                best_params = params

        return best_params

    def prepare_for_clustering(self, df: pd.DataFrame) -> (pd.DataFrame, List[str]):
        """
        Prépare les données pour le clustering en supprimant les colonnes non nécessaires et en déterminant les colonnes de polluants.
        """
        # Supprimer les colonnes non nécessaires pour le clustering
        df_dropped = df.drop(columns=["FacilityInspireID", "reportingYear"])
        
        # Récupérer les noms des colonnes des features de pollutant
        pollutant_cols = [col for col in df_dropped.columns if col not in ["eprtrSectorName", "FacilityInspireID", "reportingYear", "cluster"]]
        
        return df_dropped, pollutant_cols

    def cluster_data(self, df: pd.DataFrame, sector_col: str) -> pd.DataFrame:
        clusters_info = {}
        
        for sector in df[sector_col].unique():
            sector_data = df[df[sector_col] == sector]

            data_for_clustering, pollutant_cols = self.prepare_for_clustering(sector_data)

            scaled_data, scaler = self.scale_features(data_for_clustering, pollutant_cols)

            best_params = self.find_optimal_params(scaled_data)

            # Appliquer KMeans avec les meilleurs paramètres trouvés
            final_model = KMeans(**best_params)
            final_model.fit(scaled_data)

            # Stockage des informations de clustering
            clusters_info[sector] = {
                "scaler": scaler,
                "model": final_model
            }

            # Ajout des étiquettes de cluster au DataFrame
            df.loc[df[sector_col] == sector, "cluster"] = final_model.labels_

            # Sauvegarde du modèle
            model_filename = settings.models_path + settings.models_kmeans_names + sector + ".joblib"
            dump(final_model, model_filename)
        
        # Ajout de la colonne "sectorCluster"
        df["cluster"] = df["cluster"].astype(str)
        df["sectorCluster"] = df[sector_col] + "_" + df["cluster"]

        return df, clusters_info