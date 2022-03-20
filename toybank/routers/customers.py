from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response

from ..core.dependencies import db as s
from ..models.customer import CustomerCreate
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
