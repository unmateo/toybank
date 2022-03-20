from urllib import response


def test_new_customer_has_no_accounts(client, given_customer):
    response = client.get(f"/customers/{given_customer().id}/accounts")
    assert response.status_code == 200
    assert response.json() == []


def test_get_customer_accounts(client, given_account):
    an_account = given_account()
    response = client.get(f"/customers/{an_account.customer_id}/accounts")
    account = response.json()[0]
    assert response.status_code == 200
    assert account["id"] == an_account.id
    assert account["alias"] == an_account.alias
    assert account["balance"] == an_account.balance
    assert account["customer_id"] == an_account.customer_id


def test_create_customer_account_default_balance_is_zero(client, given_customer):
    payload = {"alias": "Savings Account"}
    response = client.post(f"/customers/{given_customer().id}/accounts", json=payload)
    account = response.json()
    assert response.status_code == 201
    assert account["balance"] == 0


def test_create_customer_account_with_initial_balance(client, given_customer):
    payload = {"alias": "Savings Account", "balance": 50}
    response = client.post(f"/customers/{given_customer().id}/accounts", json=payload)
    account = response.json()
    assert response.status_code == 201
    assert account["balance"] == 50


def test_customer_multiple_accounts(client, given_customer):
    account_a = {"alias": "Savings Account"}
    account_b = {"alias": "Retirement Account"}
    path = f"/customers/{given_customer().id}/accounts"
    client.post(path, json=account_a)
    client.post(path, json=account_b)
    response = client.get(path)
    accounts = response.json()
    assert accounts[0]["alias"] == account_a["alias"]
    assert accounts[1]["alias"] == account_b["alias"]
