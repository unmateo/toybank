from sqlalchemy import or_
from sqlalchemy.orm.session import Session

from ..models.transfer import AccountTransferCreate
from ..models.transfer import Transfer
from .accounts import AccountsService


class TransfersService:
    @staticmethod
    def create(db: Session, payload: AccountTransferCreate) -> Transfer:
        transfer = Transfer(**payload.dict())
        AccountsService.add_to_balance(
            db, payload.recipient_account_id, transfer.amount
        )
        AccountsService.add_to_balance(db, payload.sender_account_id, -transfer.amount)
        db.add(transfer)
        db.commit()
        return transfer

    @staticmethod
    def get_by_account_id(db: Session, account_id: str) -> list[Transfer]:
        criterion = or_(
            Transfer.recipient_account_id == account_id,
            Transfer.sender_account_id == account_id,
        )
        return db.query(Transfer).filter(criterion).all()
