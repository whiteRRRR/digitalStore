from services.baseService import BaseService
from repository.productRepository import ProductRepository
from schemes.productScheme import ProductScheme
from core.exception import BadRequestException

class ProductService(BaseService):
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository
        super().__init__(repository)
    
    async def create(self, scheme: ProductScheme):
        try:
            await self.repository.create(scheme)
            return "Created successful"
        except BadRequestException:
            raise BadRequestException("Bad request")

    async def get_all_product(self):
        return await self.get_all()

    async def delete_by_id(self, id: int):
        try:
            await self.repository.delete_by_id(id)
            return "Successful deleted"
        except BadRequestException:
            raise BadRequestException("Bad request")
        

