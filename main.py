from schemas import UserInput

data = {
    "name": "Moses",
    "age" : 20,
    "email": "mosesmukangai75@gmail.com"
}

user = UserInput(**data)

print(user)