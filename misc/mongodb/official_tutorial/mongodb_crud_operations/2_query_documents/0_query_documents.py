from pprint import pprint as pp

from db_conn import mongo_client

db_name = 'mongodb_example'

with mongo_client(db_name) as client:
    db = client.get_default_database()

    db.inventory.insert_many(
        [
            {
                "item": "journal",
                "qty": 25,
                "size": {"h": 14, "w": 21, "uom": "cm"},
                "status": "A",
            },
            {
                "item": "notebook",
                "qty": 50,
                "size": {"h": 8.5, "w": 11, "uom": "in"},
                "status": "A",
            },
            {
                "item": "paper",
                "qty": 100,
                "size": {"h": 8.5, "w": 11, "uom": "in"},
                "status": "D",
            },
            {
                "item": "planner",
                "qty": 75,
                "size": {"h": 22.85, "w": 30, "uom": "cm"},
                "status": "D",
            },
            {
                "item": "postcard",
                "qty": 45,
                "size": {"h": 10, "w": 15.25, "uom": "cm"},
                "status": "A",
            },
        ]
    )

    # Select All Documents in a Collection
    pp(list(db.inventory.find({})))

    # Specify Equality Condition
    pp(list(db.inventory.find({"status": "D"})))

    # Specify Conditions Using Query Operators
    pp(list(db.inventory.find({"status": {"$in": ["A", "D"]}})))

    # Specify AND Conditions
    pp(list(db.inventory.find({"status": "A", "qty": {"$lt": 30}})))

    # Specify OR Conditions
    pp(list(db.inventory.find({"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]})))

    # Specify AND as well as OR Conditions
    pp(list(db.inventory.find({"status": "A", "$or": [{"qty": {"$lt": 30}}, {"item": {"$regex": "^p"}}]})))