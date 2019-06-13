customers = {
    "name": "Taen Ahammed",
    "age": 20,
    "is_verified": True
}

print(customers["name"])
# print(customers["birthdate"])
# print(customers["Name"])

customers["name"] = "Taen"

print(customers.get("name"))
print(customers.get("birthdate"))
print(customers.get("birthdate", "Dec 12 1998"))

customers["isMarried"] = False
print(customers["isMarried"])
