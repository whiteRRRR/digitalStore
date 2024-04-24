from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from repositories.newsRepository import NewsCategoryRepository
from services.newsService import NewsCategoryService
from schemes.newsScheme import NewsScheme
from core.database import connect_database


router = APIRouter(prefix="/news_category", tags=['news_category'])

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(session: AsyncSession = Depends(connect_database)):
    news_repository = NewsCategoryRepository(session)
    news_service = NewsCategoryService(news_repository)

    return await news_service.get_all_category()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(news: NewsScheme, session: AsyncSession = Depends(connect_database)):
    news_repository = NewsCategoryRepository(session)
    news_service = NewsCategoryService(news_repository)

    return await news_service.create_category(news)

@router.delete("/{name}", status_code=status.HTTP_202_ACCEPTED)
async def delete_category_by_name(name: str, session: AsyncSession = Depends(connect_database)):
    news_repository = NewsCategoryRepository(session)
    news_service = NewsCategoryService(news_repository)
    
    return await news_service.delete_category_by_name(name)
