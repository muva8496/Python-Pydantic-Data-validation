# models.py

from pydantic import BaseModel, Field
from typing import List

class Item(BaseModel):
    product_id: str
    quantity:  int = Field(gt=0)
    price:  float  = Field(gt=0)

class Customer(BaseModel):
    customer_id: str
    email: str

class Transaction(BaseModel):
    transaction_id:str
    customer: Customer
    Items:  List[Item]


# regex  validation
from pydantic import BaseModel, field_validator
import re

class SecureTransaction(BaseModel):
    transaction_id: str

    @field_validator("transaction_id")
    @classmethod
    def validate_txn_id(cls, v):
        pattern = r"^TXN-\d{6}$"
        if not re.match(pattern, v):
            raise ValueError("Transaction ID must match TXN-XXXXXX")
        return v

# create sample payloads
payload = {
    "transaction_id": "TXN-123456",
    "customer": {
        "customer_id": "CUST001",
        "email": "user@example.com"
    },
    "items": [
        {
            "product_id": "PROD001",
            "quantity": 2,
            "price": 150.50
        }
    ]
}

# validdate payload
from models import Transaction

transaction = Transaction.model_validate(payload)

print(transaction)