customer = {
    "name": "john smith",
    "age": "30",
    "is_verified": True
}
customer["age"] = "40"
customer["living??"] = "alive"
print(customer["name"])
print(customer["age"])
print(customer["living??"])
print(customer.get("birthdate", "1 June"))
print(customer.get("an attribute that dose not exist"))