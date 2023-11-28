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
#             "n_clusters": [2, 3, 4, 5],
#             "init": ["k-means++", "random"],
#             "n_init": [10],
#             "max_iter": [300],
#             "random_state": [42]
#         }