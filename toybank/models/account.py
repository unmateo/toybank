from sqlmodel import Field
from sqlmodel import SQLModel

from .base import BaseModel


class CustomerAccountCreate(SQLModel, table=False):
    alias: str = Field(nullable=False)  #  not unique!
    balance: int = Field(nullable=True, default=0)  # no restrictions!


class AccountCreate(CustomerAccountCreate, table=False):
    customer_id: str = Field(nullable=False, foreign_key="customers.id")


class Account(AccountCreate, BaseModel, table=True):
    __tablename__ = "accounts"
