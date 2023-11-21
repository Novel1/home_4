import tortoise
from uuid import UUID
from db import models

import tortoise.exceptions

from exceptions import common as common_exc

class BaseRepo:
    model: tortoise.Model
    
    async def get_list(self, **kwargs) -> list[tortoise.Model]:
        return await self.model.filter(**kwargs)
    
    async def create(self, **kwargs) -> tortoise.Model:
        try:
            return await self.model.create(**kwargs)
        except tortoise.exceptions.IntegrityError as e:
            raise common_exc.CreateException(str(e))
        
    async def get(self, **kwargs) -> tortoise.Model:
        try:
            return await self.model.get(**kwargs)
        except tortoise.exceptions.DoesNotExist as e:
            raise common_exc.NotFoundExcepton(str(e))
        
    async def update(self, id: UUID, **kwargs) -> tortoise.Model:
        try:
            instance = await self.model.get(id=id)
            await instance.update_from_dict(kwargs).save()
            
            return instance
        except tortoise.exceptions.IntegrityError as e:
            raise common_exc.UpdateException(str(e))
        
        except tortoise.exceptions.DoesNotExist as e:
            raise common_exc.NotFoundExcepton(str(e))
        
    async def delete(self, id: UUID) -> None:
        try:
            instance = await self.model.get(id=id)
            await instance.delete
        
        except tortoise.exceptions.DoesNotExist as e:
            raise common_exc.NotFoundExcepton(str(e))
    
    
class ArticleRepositories(BaseRepo):
    model = models.Article
    