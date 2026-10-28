from pydantic import field_validator
from models import Customer

class Customer(Customer):

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email")
        return v