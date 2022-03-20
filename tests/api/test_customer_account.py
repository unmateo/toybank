def test_new_customer_has_no_accounts(client, a_customer):
    response = client.get(f"/customers/{a_customer.id}/accounts")
    assert response.status_code == 200
    assert response.json() == []


def test_get_customer_accounts(client, a_customer):
    response = client.get(f"/customers/{a_customer.id}/accounts")
    assert response.status_code == 200


def test_create_customer_account_default_balance_is_zero(client, a_customer):
    payload = {"alias": "Savings Account"}
    response = client.post(f"/customers/{a_customer.id}/accounts", json=payload)
    account = response.json()
    assert response.status_code == 201
    assert account["balance"] == 0


def test_create_customer_account_with_initial_balance(client, a_customer):
    payload = {"alias": "Savings Account", "balance": 50}
    response = client.post(f"/customers/{a_customer.id}/accounts", json=payload)
    account = response.json()
    assert response.status_code == 201
    assert account["balance"] == 50
