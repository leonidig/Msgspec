import msgspec



class Address(msgspec.Struct):
    street: str
    city: str
    country: str


class User(msgspec.Struct):
    id: int
    name: str
    age: int
    address: Address
    hobbies: list[str]
    is_active: bool


user = User(
    id=1,
    name="John Doe",
    age=30,
    address=Address(street="123 Main St", city="New York", country="USA"),
    hobbies=["reading", "gaming", "hiking"],
    is_active=True
)


json_data = msgspec.json.encode(user).decode('utf-8')
print(f"Серіалізовані дані в JSON через Msgspec: {json_data}")


def return_as_json(user_object):
    return msgspec.json.encode(user_object).decode('utf-8')


json_response = return_as_json(user)
print(f"JSON відповідь: {json_response}")


decoded_user = msgspec.json.decode(json_data.encode('utf-8'), type=User)


print(f"Декодований об'єкт: {decoded_user}")
print(f"Ім'я користувача: {decoded_user.name}")
print(f"Місто: {decoded_user.address.city}")

