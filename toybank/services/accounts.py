from sqlalchemy.orm.session import Session

from ..models.account import Account
from ..models.account import AccountCreate


class AccountsService:
    @staticmethod
    def get_by_id(db: Session, account_id: str) -> Account | None:
        return db.query(Account).get(account_id)

    @staticmethod
    def create(db: Session, payload: AccountCreate) -> Account:
        account = Account(**payload.dict())
        db.add(account)
        db.commit()
        return account

    @staticmethod
    def get_by_customer_id(db: Session, customer_id: str) -> list[Account]:
        return db.query(Account).filter_by(customer_id=customer_id).all()

    @staticmethod
    def add_to_balance(db: Session, account_id: str, amount: int) -> int:
        return (
            db.query(Account)
            .filter_by(id=account_id)
            .update({"balance": Account.balance + amount})
        )
