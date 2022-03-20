from sqlalchemy.orm.session import Session

from ..models.account import Account
from ..models.account import AccountCreate


class AccountsService:
    @staticmethod
    def create(db: Session, payload: AccountCreate) -> Account:
        account = Account(**payload.dict())
        db.add(account)
        db.commit()
        return account

    @staticmethod
    def get_by_customer_id(db: Session, customer_id: str) -> list[Account]:
        return db.query(Account).filter_by(customer_id=customer_id).all()
