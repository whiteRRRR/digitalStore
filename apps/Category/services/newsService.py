from services.baseService import BaseService
from repositories.newsRepository import NewsCategoryRepository
from schemes.newsScheme import NewsScheme
from core.exceptions import BadRequestException


class NewsCategoryService(BaseService):
    def __init__(self, news_repository: NewsCategoryRepository) -> None:
        self.news_repository = news_repository
        super().__init__(news_repository)

    async def create_category(self, news_scheme: NewsScheme) -> str:
        try:
            await self.add(news_scheme)
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
        