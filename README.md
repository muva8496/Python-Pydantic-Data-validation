Dependencies
Install required packages:
Shell
pip install pydantic
pip install pydantic[email]
The error below occurs if email validation support is missing:
Plain Text
ImportError: email-validator is not installed,
run "pip install pydantic[email]"
Example 1: Basic Validation
Python
from pydantic import BaseModel
 
class Person(BaseModel):
name: str
age: int
Invalid Input
Python
data = {
"name": "John",
"age": 15
}
Output:
Plain Text
ValidationError
Example 2: Regex Validation
Python
from pydantic import BaseModel, Field
 
class Transaction(BaseModel):
transaction_id: str = Field(
pattern=r"^TXN-\d{4}$"
)
Valid
Python
Transaction(
transaction_id="TXN-1234"
)
Invalid
Python
Transaction(
transaction_id="ABC-9999"
)
Common Errors Encountered
1. Missing Email Validator
Plain Text
ImportError: email-validator is not installed
 
Fix:
Shell
pip install pydantic[email]
2. Incorrect Regex Field Usage
Incorrect:
Python
pattern=r"^TXN-\d{4}$"
used outside a Field declaration.
Correct:
Python
transaction_id: str = Field(
pattern=r"^TXN-\d{4}$"
)
3. Undefined Model Name
Error:
Plain Text
NameError: name 'Transaction' is not defined
Cause:
Python
validated_json = Transaction.model_dump_json()
before creating/importing the model.
Fix:
Python
from schemas import Transaction
4. Calling model_dump_json Incorrectly
Error:
Plain Text
TypeError:
BaseModel.model_dump_json()
missing 1 required positional argument: 'self'
Incorrect:
Python
Transaction.model_dump_json()
Correct:
Python
transaction = Transaction(
transaction_id="TXN-1234"
)
 
transaction.model_dump_json(indent=2)
5. Undefined SalesTransaction
Error:
Plain Text
NameError: name 'SalesTransaction' is not defined
Fix:
Python
from schemas import SalesTransaction
or define the class before use.
6. Missing Required Fields
Error:
Plain Text
Field required [type=missing]
 
Example:
Python
{
"transaction_id": "TXN-1234",
"amount": 1500.0
}
Missing fields such as:
unit_price
unit_cost
profit
total_sales
sales_channel
payment_method
customer_gender
salesperson
Fix by supplying all required model fields.
JSON Serialization
Serialize validated models:
Python
transaction = Transaction(
transaction_id="TXN-1234"
)
 
print(transaction.model_dump_json(indent=2))
Output:
JSON
{
"transaction_id": "TXN-1234"
}
Lessons Learned
Pydantic v2 uses stricter validation than earlier versions.
Email validation requires an additional dependency.
Regex validation should be implemented through Field(pattern=...).
model_dump_json() is called on model instances, not classes.
Missing fields immediately trigger validation errors.
Strong schemas reduce downstream failures and improve application reliability.
References
https://docs.pydantic.dev/
https://docs.pydantic.dev/latest/concepts/models/
https://docs.pydantic.dev/latest/concepts/fields/
Status
✅ Basic validation implemented
 ✅ Regex validation implemented
 ✅ JSON serialization tested
 ✅ Error investigation completed
 ✅ Missing dependency resolved
 ⏳ Full SalesTransaction model validation in progress

Source screenshots and workbook reviewed from [image.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!sb5ea781256144a589709df7169da1df3&EntityRepresentationId=8d8bd221-9d24-4499-8712-ff3b9a27adea), [image 1.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!s752ca99196934486b3f38fa4d7ef8193&EntityRepresentationId=927bce17-04f1-4c26-af04-8b187dbf1838), [image 2.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!sa4ea9921788b40a1aa249657f210e8bd&EntityRepresentationId=079d391e-15aa-4fd6-a5b6-7e4b57340532), [image 3.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!sb961feaba7ba4af18eb60440876e955e&EntityRepresentationId=497d1627-3473-4698-b197-1e8fbd338d24), [image 4.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!s54fc7274d901426d9e50818020d64f78&EntityRepresentationId=c1881cf6-bd7a-4cb2-a6a5-3df0ec533b07), [image 5.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!s7446145e8b2444958fe549478e5470bd&EntityRepresentationId=c11f7028-4962-4c60-a1d1-b99a4288f428), [image 6.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!sd21f406326ad4462928562b031fed85d&EntityRepresentationId=b466ac5c-17b1-4dfc-a86f-959ab459561f), [image 7.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!s4a56cb061afb40c69d883c5510c8756e&EntityRepresentationId=a7dfc46e-8c00-400e-98e5-f939e5ec581a), [image 8.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!sa915654d83ca4ca59025590809fb54b8&EntityRepresentationId=9b569411-e712-41bc-8cf3-a074247f8b98), [image 9.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!se4befb10826f419c9c8e444ea6517bdc&EntityRepresentationId=09e3a6e6-5d31-4c80-bd97-2196d81da040), [image 10.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!sae03ba4de5024c7fa2e2c6893c7870be&EntityRepresentationId=21490aed-21df-4970-960d-0c31ad82b79c), [image 11.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!s215f8401c88f4bd690cdb08bbad88fd0&EntityRepresentationId=621eb4a2-bef9-4672-8dd4-6266c04f92aa), [image 12.png](https://onedrive.live.com?cid=DE2E735805B03B42&id=DE2E735805B03B42!s25399dc7cdca48238c07db1fee3fd92b&EntityRepresentationId=953d7620-feed-4565-a9cd-667c3c819704), and [vellamo_fashion_sales_fy2025_with_lookups.xlsx](https://onedrive.live.com/personal/de2e735805b03b42/_layouts/15/doc.aspx?resid=2b30a712-be8e-40bd-bd45-421ac78b57fd&cid=de2e735805b03b42&EntityRepresentationId=09c8bea6-f4c8-455f-b0db-86044bade8e0). 【1-a425f9】【2-85081e】【3-ff4797】【4-b97b71】【5-f0c8a4】【6-bd50b1】【7-39b6ea】【8-3f4864】【9-76f407】【10-df4e0d】【11-8ff781】【12-e634bf】【13-af10f0】【14-2a0fe1】"# Python-Pydantic-Data-validation" 
