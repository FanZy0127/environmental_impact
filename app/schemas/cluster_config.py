from pydantic import BaseModel

class ClusterConfig(BaseModel):
    dataset_path: str
    parameter_grid: dict 