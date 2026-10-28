from pydantic import BaseModel, field_validator

class UserInput(BaseModel):
    name: str
    age: int


    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value

data = {
    "name" : "Musa",
    "age" : 25
}

from pydantic import BaseModel, Field

from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name: str
    age: int = Field(ge=18)
    email: EmailStr

class Transaction(BaseModel):
    transaction_id: str = Field(
        pattern=r"^TXN-\d{4}$"
    )

class SalesTransaction(BaseModel):
    transaction_id: str = Field(
        pattern=r"^TXN-\d{4}$"
    )
    amount: float
try:
    t = Transaction(transaction_id="TXN-1234")
    print("Valid:", t)
except ValidationError as e:
    print(e)

from pydantic import BaseModel, Field, field_validator
from datetime import date

class SalesTransaction(BaseModel):
    transaction_id: int
    date: date

    city: str
    branch: str

    category: str
    product: str

    quantity: int = Field(gt=0)

    unit_price: float = Field(gt=0)
    unit_cost: float = Field(gt=0)

    total_sales: float
    total_cost: float
    profit: float

    sales_channel: str
    payment_method: str

    customer_gender: str
    customer_age_group: str

    salesperson: str

    @field_validator("customer_gender")
    @classmethod
    def validate_gender(cls, value):
        allowed = ["Male", "Female"]
        if value not in allowed:
            raise ValueError(f"Gender must be one of {allowed}")
        return value

    @field_validator("sales_channel")
    @classmethod
    def validate_channel(cls, value):
        allowed = ["Online", "In-Store", "Social Media"]
        if value not in allowed:
            raise ValueError(f"Invalid channel: {value}")
        return value