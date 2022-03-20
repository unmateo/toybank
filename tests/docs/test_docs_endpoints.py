from pytest import mark


@mark.parametrize("url", ["/openapi.json", "/docs", "/redoc"])
def test_doc_endpoints_are_up(client, url):
    assert client.get(url).status_code == 200
