from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response

from ..core.dependencies import db as s
from ..models.account import Account
from ..models.account import AccountCreate
from ..models.account import CustomerAccountCreate
from ..models.customer import CustomerCreate
from ..services.accounts import AccountsService
from ..services.customers import CustomersService


router = APIRouter(prefix="/customers")


@router.get("")
def get_all_customers(db=Depends(s)):
    return CustomersService.get_all(db)


@router.get("/{customer_id}")
def get_one_customer(customer_id: str, db=Depends(s)):
    customer = CustomersService.get_by_id(db, customer_id)
    if not customer:
        return Response(status_code=404)
    return customer


@router.post("", status_code=201)
def create_customer(payload: CustomerCreate, db=Depends(s)):
    return CustomersService.create(db, payload)


@router.get("/{customer_id}/accounts")
def get_customer_accounts(customer_id: str, db=Depends(s)):
    if not CustomersService.get_by_id(db, customer_id):
        return Response(status_code=404)
    return AccountsService.get_by_customer_id(db, customer_id)


@router.post("/{customer_id}/accounts", status_code=201, response_model=Account)
def create_customer_account(
    customer_id: str, payload: CustomerAccountCreate, db=Depends(s)
):
    if not CustomersService.get_by_id(db, customer_id):
        return Response(status_code=404)
    account_create = AccountCreate(customer_id=customer_id, **payload.dict())
    account = AccountsService.create(db, account_create)
    return account
