from fastapi import FastAPI

from ..routers import customers_router


def create_app():
    app = FastAPI()
    app.include_router(customers_router)
    return app
