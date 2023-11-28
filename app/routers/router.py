from fastapi import APIRouter
from app.routers import (classify, save_file, train_clustering, train_classification)

router = APIRouter()

router.include_router(save_file.router, tags=["Data"])

router.include_router(train_clustering.router, tags=["Training"])
router.include_router(train_classification.router, tags=["Training"])

router.include_router(classify.router, tags=["Classify"])