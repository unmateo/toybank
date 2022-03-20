from fastapi.testclient import TestClient
from pytest import fixture

from toybank.core.api import create_app
from toybank.core.database import engine
from toybank.core.database import get_session
from toybank.models.base import BaseModel
from toybank.models.customer import CustomerCreate
from toybank.services.customers import CustomersService


@fixture(autouse=True)
def db_schema():
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


@fixture
def db():
    with get_session() as s:
        yield s


@fixture
def app():
    return create_app()


@fixture
def client(app):
    return TestClient(app)


@fixture
def a_customer(db):
    c = CustomerCreate(email="customer@example.com")
    return CustomersService.create(db, c)
