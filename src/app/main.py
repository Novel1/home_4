import fastapi
import pydantic

from api.router import router

from tortoise.contrib.fastapi import register_tortoise
from db.conf import TORTOISE_ORM

from exceptions import handlers as exc_handlers, http as http_exc



def setup():
    app = fastapi.FastAPI()
    app.include_router(router)

    register_tortoise(app=app, config=TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True)
    
    app.exception_handler(pydantic.ValidationError)(exc_handlers.query_params_exc_handler) 
    app.exception_handler(http_exc.BaseHTTPException)(exc_handlers.request_exc_handler) 
    app.exception_handler(500)(exc_handlers.internal_exc_handler) 

    return app

   
app = setup()


if __name__ == "__main__":
    import uvicorn


    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)