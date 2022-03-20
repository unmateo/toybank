from toybank.services.accounts import AccountsService


def test_new_customer_account_has_no_transfers(client, given_account):
    an_account = given_account()
    response = client.get(
        f"/customers/{an_account.customer_id}/accounts/{an_account.id}/transfers"
    )
    assert response.status_code == 200
    assert response.json() == []


def test_get_customer_account_transfers(client, db, given_transfer):
    transfer = given_transfer()
    sender_account = AccountsService.get_by_id(db, transfer.sender_account_id)
    recipient_account = AccountsService.get_by_id(db, transfer.recipient_account_id)

    sender_response = client.get(
        f"/customers/{sender_account.customer_id}/accounts/{sender_account.id}/transfers"
    )
    assert sender_response.status_code == 200
    sender_transfer = sender_response.json()[0]
    assert sender_transfer.pop("created_at") == transfer.created_at.isoformat()
    assert sender_transfer == transfer.dict(exclude={"created_at"})

    recipient_response = client.get(
        f"/customers/{recipient_account.customer_id}/accounts/{recipient_account.id}/transfers"
    )
    assert recipient_response.status_code == 200
    recipient_transfer = recipient_response.json()[0]
    assert recipient_transfer.pop("created_at") == transfer.created_at.isoformat()
    assert recipient_transfer == transfer.dict(exclude={"created_at"})


def test_create_customer_account_transfer(client, db, given_account, caplog):
    account_a = given_account()
    account_b = given_account()
    payload = {"recipient_account_id": account_b.id, "amount": 100}
    response = client.post(
        f"/customers/{account_a.customer_id}/accounts/{account_a.id}/transfers",
        json=payload,
    )
    transfer = response.json()
    assert response.status_code == 201
    assert transfer["amount"] == 100
    assert transfer["sender_account_id"] == account_a.id
    db.refresh(account_a)
    db.refresh(account_b)
    assert account_a.balance == -100
    assert account_b.balance == 100
