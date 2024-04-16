from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.newsRepository import NewsRepository
from services.newsService import NewsService
from schemes.newsScheme import NewsScheme
from core.database import connection_base


router = APIRouter(prefix="/news_category", tags=['category'])

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(session: AsyncSession = Depends(connection_base)):
    news_repository = NewsRepository(session)
    news_service = NewsService(news_repository)

    return await news_service.get_all_category()

@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_category(news: NewsScheme, session: AsyncSession = Depends(connection_base)):
    news_repository = NewsRepository(session)
    news_service = NewsService(news_repository)

    return await news_service.create_category(news)

@router.delete("delete/{name}", status_code=status.HTTP_200_OK)
async def delete_category_by_name(name: str, session: AsyncSession = Depends(connection_base)):
    news_repository = NewsRepository(session)
    news_service = NewsService(news_repository)
    
    return await news_service.delete_category_by_name(name)
