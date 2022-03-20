def test_get_all_customers_no_customers(client):
    response = client.get("/customers")
    assert response.status_code == 200


def test_get_all_customers_with_customers(client, a_customer):
    response = client.get("/customers")
    assert response.status_code == 200
    assert_is_customer_response(a_customer, response.json()[0])


def test_get_one_customer(client, a_customer):
    response = client.get(f"/customers/{a_customer.id}")
    assert response.status_code == 200
    assert_is_customer_response(a_customer, response.json())


def test_get_unexistent_customer_returns_not_found(client):
    response = client.get("/customers/1")
    assert response.status_code == 404


def test_create_customer(client):
    payload = {"email": "some_email@example.com"}
    response = client.post("/customers", json=payload)
    assert response.status_code == 201


def assert_is_customer_response(customer, response):
    assert response["id"] == customer.id
    assert response["created_at"] == customer.created_at.isoformat()
    assert response["email"] == customer.email
