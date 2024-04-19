from fastapi import APIRouter
from api.v1.endpoints.news import router as news_router
from api.v1.endpoints.product import router as product_router

router = APIRouter()
router.include_router(news_router)
router.include_router(product_router)

