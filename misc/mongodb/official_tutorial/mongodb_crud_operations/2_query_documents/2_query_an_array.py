from pprint import pprint as pp

from db_conn import mongo_client

db_name = 'mongodb_example'

with mongo_client(db_name) as client:
    db = client.get_default_database()

    # db.inventory.insert_many(
    #     [
    #         {"item": "journal", "qty": 25, "tags": ["blank", "red"], "dim_cm": [14, 21]},
    #         {"item": "notebook", "qty": 50, "tags": ["red", "blank"], "dim_cm": [14, 21]},
    #         {
    #             "item": "paper",
    #             "qty": 100,
    #             "tags": ["red", "blank", "plain"],
    #             "dim_cm": [14, 21],
    #         },
    #         {"item": "planner", "qty": 75, "tags": ["blank", "red"], "dim_cm": [22.85, 30]},
    #         {"item": "postcard", "qty": 45, "tags": ["blue"], "dim_cm": [10, 15.25]},
    #     ]
    # )

    # elements and order
    pp(list(db.inventory.find({"tags": ["red", "blank"]})))
    # just elements
    pp(list(db.inventory.find({"tags": {"$all": ["red", "blank"]}})))
    # contains specified element
    pp(list(db.inventory.find({"tags": "red"})))
    # contains at least one element whose value is greater than 25
    pp(list(db.inventory.find({"dim_cm": {"$gt": 25}})))

    # Specify Multiple Conditions for Array Elements
    # Query an Array with Compound Filter Conditions on the Array Elements
    # one element can satisfy the greater than 15 condition and another element can satisfy the less than 20 condition,
    # or a single element can satisfy both
    pp(list(db.inventory.find({"dim_cm": {"$gt": 15, "$lt": 20}})))

    # Query for an Array Element that Meets Multiple Criteria
    # contains at least one element that is both greater than ($gt) 22 and less than ($lt) 30
    pp(list(db.inventory.find({"dim_cm": {"$elemMatch": {"$gt": 22, "$lt": 30}}})))

    # Query for an Element by the Array Index Position
    # the second element in the array dim_cm is greater than 25
    pp(list(db.inventory.find({"dim_cm.1": {"$gt": 25}})))

    # Query an Array by Array Length
    # tags has 3 elements
    pp(list(db.inventory.find({"tags": {"$size": 3}})))
