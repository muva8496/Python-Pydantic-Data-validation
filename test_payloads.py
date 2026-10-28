bad_payload = {
    "transaction_id": "BAD-ID",
    "customer": {
        "customer_id": "CUST001",
        "email": "invalid-email"
    },
    "items": [
        {
            "product_id": "PROD001",
            "quantity": -1,
            "price": 150.50
        }
    ]
}

try:
    Transaction.model_validate(bad_payload)
except Exception as e:
    print(e)



from schemas import Transaction, SalesTransaction

transaction = Transaction(
    transaction_id="TXN-1234"
)

print(transaction.model_dump_json(indent=2))

sale = SalesTransaction(
    transaction_id="TXN-1234",
    amount=1500.0
)

print(sale.model_dump_json(indent=2))

print(validated_json)

transaction = SalesTransaction(
    transaction_id=100001,
    date="2025-01-01",
    city="Nairobi",
    branch="Vellamo Karen",
    category="Shoes",
    product="Heeled Sandals",
    quantity=1,
    unit_price=3400,
    unit_cost=1970,
    total_sales=3400,
    total_cost=1970,
    profit=1430,
    sales_channel="In-Store",
    payment_method="M-Pesa",
    customer_gender="Female",
    customer_age_group="25-34",
    salesperson="Kipchoge N."
)

print(transaction)


bad_record = {
    "transaction_id": 100001,
    "date": "2025-01-01",
    "city": "Nairobi",
    "branch": "Vellamo Karen",
    "category": "Shoes",
    "product": "Heeled Sandals",
    "quantity": -5,
    "unit_price": -100,
    "unit_cost": 1970,
    "total_sales": 3400,
    "total_cost": 1970,
    "profit": 1430,
    "sales_channel": "TikTok",
    "payment_method": "M-Pesa",
    "customer_gender": "Unknown",
    "customer_age_group": "25-34",
    "salesperson": "Kipchoge N."
}

SalesTransaction(**bad_record)

from pydantic import model_validator

class SalesTransaction(BaseModel):
    # fields here ...

    @model_validator(mode="after")
    def verify_calculations(self):
        expected_sales = self.quantity * self.unit_price

        if self.total_sales != expected_sales:
            raise ValueError(
                f"Total Sales should be {expected_sales}"
            )

        return self