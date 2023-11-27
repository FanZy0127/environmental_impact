from fastapi import APIRouter
from app.routers import (save_file, predict, train_clustering, train_classification)

router = APIRouter()

router.include_router(save_file.router, tags=["Data"])

router.include_router(train_clustering.router, tags=["Training"])
router.include_router(train_classification.router, tags=["Training"])

router.include_router(predict.router, tags=["Predict"])