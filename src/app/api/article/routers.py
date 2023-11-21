from api.shema import ArticleSchema, ArticleGetShema
import fastapi as fa
from db.repository import ArticleRepositories
from uuid import UUID
from exceptions import common as common_exc, http as http_exc

router = fa.APIRouter(prefix='/article')
repo = ArticleRepositories()


@router.get('')
async def get_articles(query: ArticleGetShema = fa.Depends()):
    return await repo.get_list(**query.model_dump())


@router.get('/{id}')
async def get_article(id: UUID):
    try:
        return await repo.get(id)
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    
@router.post('')
async def create_article(body: ArticleSchema):
    try:
        return await repo.create(**body.model_dump())
    
    except common_exc.CreateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    
@router.patch('/{id}')
async def update_article(id: UUID, body: ArticleSchema):
    try:
        return await repo.update(id, **body.model_dump())
    
    except common_exc.UpdateException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))
    
@router.delete('/{id}')
async def delete_article(id: UUID):
    try:
        return await repo.delete(id)
    
    except common_exc.DeleteException as e:
        raise http_exc.HTTPBadRequestException(detail=str(e))
    
    except common_exc.NotFoundExcepton as e:
        raise http_exc.HTTPNotFoundException(detail=str(e))