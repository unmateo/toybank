from fastapi.testclient import TestClient
from pytest import fixture

from toybank.app import app


@fixture
def client():
    return TestClient(app)
