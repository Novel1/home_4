from fastapi import APIRouter
from api.article.routers import router as article_router


router = APIRouter(prefix='/api')
router.include_router(article_router)

@router.get('/greetings')
def get_greetings():
    return {'text': 'Greetings!'}