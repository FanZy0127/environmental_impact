from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/predict",
    description="Attribue une note écologique à une entreprise.",
)
def predict():
    """
    3. Prediction 
        1.1 Récupère la donnée en input
        1.2 Transforme?
        1.3 Clustering
        1.4 Classification
    """
    pass