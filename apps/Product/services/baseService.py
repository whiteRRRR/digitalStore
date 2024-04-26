class BaseService:
    def __init__(self, repository) -> None:
        self.repository = repository

    async def add(self, scheme):
        await self.repository.create(scheme)

    async def get_all(self):
        await self.repository.read_all()
    
    async def get_by_id(self, id: int):
        await self.repository.read_by_id(id)
    
    async def update_by_id(self, scheme, id: int):
        await self.repository.update_by_id(scheme, id)
    
    async def delete_by_id(self, id: int):
        await self.repository.delete_by_id(id)
    