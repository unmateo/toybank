from sqlmodel import Field
from sqlmodel import SQLModel

from .base import BaseModel


class CustomerCreate(SQLModel, table=False):
    email: str = Field(nullable=False)  #  not unique!


class Customer(CustomerCreate, BaseModel, table=True):
    __tablename__ = "customers"
