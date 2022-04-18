import redis
from redis.commands.json.path import Path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Adding a JSON document to an index
user1 = {
    "user": {
        "name": "Paul John",
        "email": "paul.john@example.com",
        "age": 42,
        "city": "London"
    }
}

user2 = {
    "user": {
        "name": "Eden Zamir",
        "email": "eden.zamir@example.com",
        "age": 29,
        "city": "Tel Aviv"
    }
}

user3 = {
    "user": {
        "name": "Paul Zamir",
        "email": "paul.zamir@example.com",
        "age": 35,
        "city": "Tel Aviv"
    }
}

r.json().set("user:1", Path.rootPath(), user1)
r.json().set("user:2", Path.rootPath(), user2)
r.json().set("user:3", Path.rootPath(), user3)

schema = (
    TextField("$.user.name", as_name="name"),
    TagField("$.user.city", as_name="city"),
    NumericField("$.user.age", as_name="age")
)

r.ft().create_index(schema, definition=IndexDefinition(prefix=["user:"], index_type=IndexType.JSON))

# Searching
# Simple search
print(r.ft().search("Paul"))

# Filtering search results
q1 = Query("Paul").add_filter(NumericFilter("age", 30, 40))
print(r.ft().search(q1))

# Projecting using JSON Path expressions
print(r.ft().search(Query("Paul").return_field("$.user.city", as_field="city")).docs)

# Aggregation
req = aggregations.AggregateRequest("Paul").sort_by("@age")
print(r.ft().aggregate(req).rows)
