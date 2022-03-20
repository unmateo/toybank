from json import dump
from json import load

from pytest import mark


OPENAPI = "tests/docs/openapi.json"


@mark.parametrize("url", ["/openapi.json", "/docs", "/redoc"])
def test_doc_endpoints_are_up(client, url):
    assert client.get(url).status_code == 200


def test_openapi(client):
    """Tracks changes in API spec."""
    openapi = client.get("/openapi.json").json()
    # dump_openapi(openapi)
    with open(OPENAPI) as file:
        expected = load(file)
    assert openapi == expected


def dump_openapi(openapi):
    with open(OPENAPI, "w") as file:
        dump(openapi, file, indent=4)
