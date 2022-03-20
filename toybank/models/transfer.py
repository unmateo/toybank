from sqlmodel import Field
from sqlmodel import SQLModel

from .base import BaseModel


class CustomerAccountTransferCreate(SQLModel, table=False):
    recipient_account_id: str = Field(nullable=False, foreign_key="accounts.id")
    amount: int = Field(nullable=False, gt=0)


class AccountTransferCreate(CustomerAccountTransferCreate, table=False):
    sender_account_id: str = Field(nullable=False, foreign_key="accounts.id")


class Transfer(AccountTransferCreate, BaseModel, table=True):
    __tablename__ = "transfers"
