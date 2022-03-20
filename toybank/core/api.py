from fastapi import FastAPI

from ..routers import customers


def create_app() -> FastAPI:
    app = FastAPI(title="Toybank")
    app.include_router(customers)
    return app
