class BaseService:
    def __init__(self, repository):
        self.repository = repository

    async def get_by_id(self, id: int):
        return await self.repository.read_by_id(id)

    async def add(self, schema):
        return await self.repository.create(schema)

    async def update_by_id(self, id: int, schema):
        return await self.repository.update_by_id(id, schema)

    async def delete_by_id(self, id: int):
        return await self.repository.delete_by_id(id)
