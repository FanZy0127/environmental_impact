from app.schemas.cluster_config import ClusterConfig
from app.config.settings import settings

def get_cluster_config() -> ClusterConfig:
    return ClusterConfig(
        dataset_path=settings.files_path + settings.air_dataset,
        parameter_grid={
            "n_clusters": [2],
            "init": ["k-means++"],
            "n_init": [10],
            "max_iter": [10],
            "random_state": [42]
        }
    )

# parameter_grid={
#     "n_clusters": [2, 3, 4, 5],  # nbre de clusters à former
#     "init": ["k-means++", "random"],  # définit comment les centres initiaux de clusters sont définis
#     "n_init": [10],  # nbre de fois que l'algorithme sera éxécuté
#     "max_iter": [300],  # nbre max d'itérations pour une seule éxécution
#     "random_state": [42]  # reproduction des résultats
# }