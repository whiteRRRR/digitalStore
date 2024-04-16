from services.baseService import BaseService
from repositories.newsRepository import NewsRepository

class NewsService(BaseService):
    def __init__(self, news_repository: NewsRepository) -> None:
        self.news_repository = news_repository

        super().__init__(news_repository)

    async def create_category(self, scheme) -> str:
        try:
            await self.add(scheme)
            return "News category created successfull"
        except Exception:
            raise Exception("category not created")
    
    async def delete_category_by_name(self, name: str) -> str:
        try:
            category_info = self.news_repository.read_by_name(name)
            await self.delete_by_id(category_info.id)
            return "Category deleted successfull"
        except Exception:
            raise Exception("category not deleted")
        