from sqlalchemy.orm.session import Session

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
    def get_by_id(db: Session, customer_id: str) -> Customer | None:
        return db.query(Customer).get(customer_id)

    @staticmethod
    def get_all(db: Session) -> list[Customer]:
        return db.query(Customer).all()
