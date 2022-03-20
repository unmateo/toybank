from fastapi.testclient import TestClient
from pytest import fixture

from toybank.core.api import create_app
from toybank.core.database import engine
from toybank.core.database import get_session
from toybank.models.account import AccountCreate
from toybank.models.base import BaseModel
from toybank.models.customer import CustomerCreate
from toybank.services.accounts import AccountsService
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
def given_customer(db):
    def create_customer(email="customer@example.com"):
        c = CustomerCreate(email=email)
        return CustomersService.create(db, c)

    return create_customer


@fixture
def given_account(db, given_customer):
    default_customer = given_customer()

    def create_account(alias="Savings Accoount", customer=default_customer, balance=0):
        a = AccountCreate(alias=alias, customer_id=customer.id, balance=balance)
        return AccountsService.create(db, a)

    return create_account
