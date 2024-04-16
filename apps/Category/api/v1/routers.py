from fastapi import APIRouter
from api.v1.endpoints.news import router as news_router


router = APIRouter()
router.include_router(news_router)

