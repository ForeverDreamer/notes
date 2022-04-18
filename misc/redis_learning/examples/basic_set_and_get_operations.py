import redis

r = redis.Redis(decode_responses=True)

print(r.ping())

# The most basic usage of set and get
print(r.set("full_name", "john doe"))

print(r.exists("full_name"))

print(r.get("full_name"))

# We can override the existing value by calling set method for the same key
r.set("full_name", "overridee!")

print(r.get("full_name"))

# It is also possible to pass an expiration value to the key by using setex method
r.setex("important_key", 100, "important_value")

r.ttl("important_key")

# A dictionary can be inserted like this
dict_data = {
    "employee_name": "Adam Adams",
    "employee_age": 30,
    "position": "Software Engineer",
}

r.mset(dict_data)

# To get multiple keys’ values, we can use mget. If a non-existing key is also passed, Redis return None for that key
print(r.mget("employee_name", "employee_age", "position", "non_existing"))
