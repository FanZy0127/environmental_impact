from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/train_classification",
    description="Entraine le modèle de classification avec un nouveau dataset.",
)
def train_classification():
    """
    2. Entrainement classification
        1.1 Récupère dataset
        1.2 Transforme
        1.3 Utilisation clustering pour feature
        1.4 Labellisation
        1.5 Classification
    """
    pass