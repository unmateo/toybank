from sqlalchemy.orm.session import Session

from ..core.exceptions import NotFound
from ..models.customer import Customer
from ..models.customer import CustomerCreate


class CustomersService:
    @staticmethod
    def create(db: Session, payload: CustomerCreate) -> Customer:
        customer = Customer(**payload.dict())
        db.add(customer)
        db.commit()
        return customer

    @staticmethod
    def get_by_id(db: Session, customer_id: str) -> Customer:
        customer = db.query(Customer).get(customer_id)
        if not customer:
            raise NotFound(f"Couldn't find Customer {customer_id}")
        return customer

    @staticmethod
    def get_all(db: Session) -> list[Customer]:
        return db.query(Customer).all()
