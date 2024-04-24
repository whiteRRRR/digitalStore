from fastapi import APIRouter, Depends, status
from core.database import connect_database
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.productScheme import ProductCategoryScheme
from repositories.productRepository import ProductCategoryRepository
from services.productService import ProductCategoryService

router = APIRouter(prefix="/product_category", tags=["product_category"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(session: AsyncSession = Depends(connect_database)):
    product_repository = ProductCategoryRepository(session)
    product_service = ProductCategoryService(product_repository)

    return await product_service.get_all()

@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_category(product_category: ProductCategoryScheme, session: AsyncSession = Depends(connect_database)):
    product_repository = ProductCategoryRepository(session)
    product_service = ProductCategoryService(product_repository)

    return await product_service.create_category(product_category)

@router.delete("/delete/{name}", status_code=status.HTTP_200_OK)
async def delete_category_by_name(name: str, session: AsyncSession = Depends(connect_database)):
    product_repository = ProductCategoryRepository(session)
    product_service = ProductCategoryService(product_repository)
    
    return await product_service.delete_category_by_name(name)
