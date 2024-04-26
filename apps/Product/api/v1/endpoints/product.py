from fastapi import APIRouter, Depends, status
from core.database import connection_database
from repository.productRepository import ProductRepository
from services.productService import ProductService
from schemes.productScheme import ProductScheme
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="product/", tags=["product"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(scheme: ProductScheme, session: AsyncSession = Depends(connection_database)):
    repository = ProductRepository(session)
    service = ProductService(repository)

    return await service.create(scheme)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(session: AsyncSession = Depends(connection_database)):
    repository = ProductRepository(session)
    service = ProductService(repository)

    return await service.get_all_product()

@router.delete("/", status_code=status.HTTP_201_CREATED)
async def delete_by_id(id, session: AsyncSession = Depends(connection_database)):
    repository = ProductRepository(session)
    service = ProductService(repository)

    return service.delete_by_id(id)
    