from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response

from ..core.dependencies import db as s
from ..models.account import Account
from ..models.account import AccountCreate
from ..models.account import CustomerAccountCreate
from ..models.customer import CustomerCreate
from ..models.transfer import AccountTransferCreate
from ..models.transfer import CustomerAccountTransferCreate
from ..models.transfer import Transfer
from ..services.accounts import AccountsService
from ..services.customers import CustomersService
from ..services.transfers import TransfersService
from toybank.core.enums import RouterTags


customers = APIRouter(prefix="/customers")


@customers.get("", tags=[RouterTags.CUSTOMERS])
def get_all_customers(db=Depends(s)):
    return CustomersService.get_all(db)


@customers.get("/{customer_id}", tags=[RouterTags.CUSTOMERS])
def get_one_customer(customer_id: str, db=Depends(s)):
    return CustomersService.get_by_id(db, customer_id)


@customers.post("", status_code=201, tags=[RouterTags.CUSTOMERS])
def create_customer(payload: CustomerCreate, db=Depends(s)):
    return CustomersService.create(db, payload)


@customers.get(
    "/{customer_id}/accounts", tags=[RouterTags.CUSTOMERS, RouterTags.ACCOUNTS]
)
def get_customer_accounts(customer_id: str, db=Depends(s)):
    CustomersService.get_by_id(db, customer_id)
    return AccountsService.get_by_customer_id(db, customer_id)


@customers.post(
    "/{customer_id}/accounts",
    status_code=201,
    response_model=Account,
    tags=[RouterTags.CUSTOMERS, RouterTags.ACCOUNTS],
)
def create_customer_account(
    customer_id: str, payload: CustomerAccountCreate, db=Depends(s)
):
    CustomersService.get_by_id(db, customer_id)
    account_create = AccountCreate(customer_id=customer_id, **payload.dict())
    account = AccountsService.create(db, account_create)
    return account


@customers.post(
    "/{customer_id}/accounts/{account_id}/transfers",
    status_code=201,
    response_model=Transfer,
    tags=[RouterTags.CUSTOMERS, RouterTags.ACCOUNTS, RouterTags.TRANSFERS],
)
def create_transfer(
    customer_id: str,
    account_id: str,
    payload: CustomerAccountTransferCreate,
    db=Depends(s),
):
    CustomersService.get_by_id(db, customer_id)
    account = AccountsService.get_by_id(db, account_id)
    if account.customer_id != customer_id:
        return Response(status_code=400)
    transfer_create = AccountTransferCreate(
        sender_account_id=account_id, **payload.dict()
    )
    transfer = TransfersService.create(db, transfer_create)
    return transfer


@customers.get(
    "/{customer_id}/accounts/{account_id}/transfers",
    status_code=200,
    tags=[RouterTags.CUSTOMERS, RouterTags.ACCOUNTS, RouterTags.TRANSFERS],
)
def get_account_transfers(
    customer_id: str,
    account_id: str,
    db=Depends(s),
):
    CustomersService.get_by_id(db, customer_id)
    account = AccountsService.get_by_id(db, account_id)
    if account.customer_id != customer_id:
        return Response(status_code=400)
    return TransfersService.get_by_account_id(db, account_id)
