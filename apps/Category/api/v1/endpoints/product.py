from fastapi import APIRouter, Depends, status
from core.database import connection_base
from sqlalchemy.ext.asyncio import AsyncSession
from schemes.productScheme import ProductCategoryScheme
from repositories.productRepository import ProductRepository
from services.productService import ProductService


router = APIRouter(prefix="/product_category", tags=["product"])

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(session: AsyncSession = Depends(connection_base)):
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)

    return await product_service.get_all_category()

@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_category(product_category: ProductCategoryScheme, session: AsyncSession = Depends(connection_base)):
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)

    return await product_service.create_category(product_category)

@router.delete("/delete/{name}", status_code=status.HTTP_200_OK)
async def delete_category_by_name(name: str, session: AsyncSession = Depends(connection_base)):
    product_repository = ProductRepository(session)
    product_service = ProductService(product_repository)
    
    return await product_service.delete_category_by_name(name)