from uuid import UUID
import pydantic

class ArticleSchema(pydantic.BaseModel):
    name: str
    description: str
    
    
class ArticleGetShema(ArticleSchema):
    id: UUID