from pprint import pprint as pp

# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
from bson.son import SON

from db_conn import mongo_client

db_name = 'mongodb_example'

with mongo_client(db_name) as client:
    db = client.get_default_database()

    # db.inventory.insert_many(
    #     [
    #         {
    #             "item": "journal",
    #             "instock": [
    #                 SON([("warehouse", "A"), ("qty", 5)]),
    #                 SON([("warehouse", "C"), ("qty", 15)]),
    #             ],
    #         },
    #         {"item": "notebook", "instock": [SON([("warehouse", "C"), ("qty", 5)])]},
    #         {
    #             "item": "paper",
    #             "instock": [
    #                 SON([("warehouse", "A"), ("qty", 60)]),
    #                 SON([("warehouse", "B"), ("qty", 15)]),
    #             ],
    #         },
    #         {
    #             "item": "planner",
    #             "instock": [
    #                 SON([("warehouse", "A"), ("qty", 40)]),
    #                 SON([("warehouse", "B"), ("qty", 5)]),
    #             ],
    #         },
    #         {
    #             "item": "postcard",
    #             "instock": [
    #                 SON([("warehouse", "B"), ("qty", 15)]),
    #                 SON([("warehouse", "C"), ("qty", 35)]),
    #             ],
    #         },
    #     ]
    # )

    # Query for a Document Nested in an Array
    #  require an exact match of the specified document, including the field order
    pp(list(db.inventory.find({"instock": SON([("warehouse", "A"), ("qty", 5)])})))

    # Specify a Query Condition on a Field in an Array of Documents
    # Specify a Query Condition on a Field Embedded in an Array of Documents
    # instock array has at least one embedded document that contains the field qty whose value is less than or equal to 20
    pp(list(db.inventory.find({"instock.qty": {"$lte": 20}})))

    # Use the Array Index to Query for a Field in the Embedded Document
    # instock array has as its first element a document that contains the field qty whose value is less than or equal to 20
    pp(list(db.inventory.find({"instock.0.qty": {"$lte": 20}})))

    # Specify Multiple Conditions for Array of Documents
    # A Single Nested Document Meets Multiple Query Conditions on Nested Fields
    # instock array has at least one embedded document that contains both the field qty equal to 5 and the field warehouse equal to A
    pp(list(db.inventory.find({"instock": {"$elemMatch": {"qty": 5, "warehouse": "A"}}})))
    # instock array has at least one embedded document that contains the field qty that is greater than 10 and less than or equal to 20
    pp(list(db.inventory.find({"instock": {"$elemMatch": {"qty": {"$gt": 10, "$lte": 20}}}})))

    # Combination of Elements Satisfies the Criteria
    # instock array has the qty field greater than 10 and any document (but not necessarily the same embedded document)
    # in the array has the qty field less than or equal to 20
    pp(list(db.inventory.find({"instock.qty": {"$gt": 10, "$lte": 20}})))
    # instock array has at least one embedded document that contains the field qty equal to 5 and at least one embedded
    # document (but not necessarily the same embedded document) that contains the field warehouse equal to A
    pp(list(db.inventory.find({"instock.qty": 5, "instock.warehouse": "A"})))
