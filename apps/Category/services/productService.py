from services.baseService import BaseService
from core.exceptions import BadRequestException
from repositories.productRepository import ProductCategory
from schemes.productScheme import ProductCategoryScheme

class ProductService(BaseService):
    def __init__(self, product_repository: ProductCategory):
        self.product_repository = product_repository
        super().__init__(product_repository)
    
    async def create_category(self, product_scheme: ProductCategoryScheme) -> str:
        try:
            await self.add(product_scheme: ProductCategoryScheme)
            return "News category created successfull"
        except BadRequestException:
            raise BadRequestException("category not created")

    async def get_all_category(self):
        categories = await self.get_all()
        if categories:
            return categories
        raise BadRequestException("category not deleted")
    
    async def delete_category_by_name(self, name: str) -> str:
        try:
            category_info = await self.news_repository.read_by_name(name)
            await self.delete_by_id(category_info.id)
            return "Category deleted successfull"
        except BadRequestException:
            raise BadRequestException("category not deleted")
        