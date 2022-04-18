from pprint import pprint as pp

# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
from bson.son import SON

from db_conn import mongo_client

db_name = 'mongodb_example'

with mongo_client(db_name) as client:
    db = client.get_default_database()

    db.inventory.insert_many(
        [
            {
                "item": "journal",
                "qty": 25,
                "size": SON([("h", 14), ("w", 21), ("uom", "cm")]),
                "status": "A",
            },
            {
                "item": "notebook",
                "qty": 50,
                "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
                "status": "A",
            },
            {
                "item": "paper",
                "qty": 100,
                "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
                "status": "D",
            },
            {
                "item": "planner",
                "qty": 75,
                "size": SON([("h", 22.85), ("w", 30), ("uom", "cm")]),
                "status": "D",
            },
            {
                "item": "postcard",
                "qty": 45,
                "size": SON([("h", 10), ("w", 15.25), ("uom", "cm")]),
                "status": "A",
            },
        ]
    )

    # Match an Embedded/Nested Document
    # match
    pp(list(db.inventory.find({"size": SON([("h", 14), ("w", 21), ("uom", "cm")])})))
    # Doesn't match
    pp(list(db.inventory.find({"size": SON([("w", 21), ("h", 14), ("uom", "cm")])})))

    # Query on Nested Field
    # Specify Equality Match on a Nested Field
    pp(list(db.inventory.find({"size.uom": "in"})))

    # Specify Match using Query Operator
    pp(list(db.inventory.find({"size.h": {"$lt": 15}})))

    # Specify AND Condition
    pp(list(db.inventory.find({"size.h": {"$lt": 15}, "size.uom": "in", "status": "D"})))
