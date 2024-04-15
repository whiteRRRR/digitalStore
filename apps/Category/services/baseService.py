class BaseService:
    def __init__(self, repository):
        self.repository = repository
    
    async def add(self, scheme):
        return await self.repository.create(scheme)

    async def get_by_id(self, id: int):
        return await self.repository.read_by_id(id)
    
    async def update_by_id(self, id: int, scheme):
        return await self.repository.update_by_id(id, scheme)
    
    async def delete_by_id(self, id: int):
        return await self.repository.delete_by_id(id)