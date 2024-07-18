import uuid
from datetime import datetime

import ormar

from app.database.config import BaseMeta


class Client(ormar.Model):
    class Meta(BaseMeta):
        tablename = "client"

    id: int = ormar.Integer(primary_key=True)
    UUID: uuid.UUID = ormar.UUID(default=uuid.uuid4, unique=True, nullable=False, name="uuid")
    name: str = ormar.String(max_length=255, nullable=False, name="name")
    company: str = ormar.String(max_length=255, nullable=True, name="company")
    product_type: str = ormar.String(max_length=255, nullable=True, name="product_type")
    document_identifier: str = ormar.String(max_length=100, nullable=True, name="document_identifier")
    date_created: datetime = ormar.DateTime(default=datetime.now, name="date_created")
    date_updated: datetime = ormar.DateTime(default=datetime.now, onupdate=datetime.now, name="date_updated")


class Debt(ormar.Model):
    class Meta(BaseMeta):
        tablename = "debt"

    id: int = ormar.Integer(primary_key=True)
    emition_date: datetime = ormar.DateTime(nullable=False, name="emition_date")
    debt_amount: float = ormar.Decimal(max_digits=10, decimal_places=2, nullable=False, name="debt_amount")
    minimum_payment: float = ormar.Decimal(max_digits=10, decimal_places=2, nullable=True, name="minimum_payment")
    debt_default: bool = ormar.Boolean(nullable=True, name="debt_default")


class Payment(ormar.Model):
    class Meta(BaseMeta):
        tablename = "payment"

    id: int = ormar.Integer(primary_key=True)
    transaction_date: datetime = ormar.DateTime(nullable=False, name="transaction_date")
    payment_gateway: str = ormar.String(max_length=255, nullable=True, name="payment_gateway")
    bank_code: str = ormar.String(max_length=255, nullable=True, name="bank_code")
    operation_identifier: str = ormar.String(max_length=255, nullable=True, name="operation_identifier")
    payment_type: str = ormar.String(max_length=255, nullable=True, name="payment_type")
    query_type: str = ormar.String(max_length=255, nullable=True, name="query_type")
    client_id: int = ormar.ForeignKey(Client, related_name="payments", nullable=False, name="client_id")
    product_code: str = ormar.String(max_length=255, nullable=True, name="product_code")
    debt_id: int = ormar.ForeignKey(Debt, related_name="payments", nullable=True, name="debt_id")
    currency: str = ormar.String(max_length=10, nullable=True, name="currency")
    total_to_pay: float = ormar.Decimal(max_digits=10, decimal_places=2, nullable=True, name="total_to_pay")
    date_created: datetime = ormar.DateTime(default=datetime.now, name="Date_created")
    created_by: str = ormar.String(max_length=255, nullable=True, name="created_by")
    date_updated: datetime = ormar.DateTime(default=datetime.now, onupdate=datetime.now, name="date_updated")
    updated_by: str = ormar.String(max_length=255, nullable=True, name="updated_by")
