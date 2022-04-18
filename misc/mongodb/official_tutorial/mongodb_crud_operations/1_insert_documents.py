from db_conn import mongo_client

db_name = 'mongodb_example'

with mongo_client(db_name) as client:
    db = client.get_default_database()

    # Insert a Single Document
    result = db.inventory.insert_one(
        {
            "item": "canvas",
            "qty": 100,
            "tags": ["cotton"],
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
        }
    )
    print(result)

    # Insert Multiple Documents
    result = db.inventory.insert_many(
        [
            {
                "item": "journal",
                "qty": 25,
                "tags": ["blank", "red"],
                "size": {"h": 14, "w": 21, "uom": "cm"},
            },
            {
                "item": "mat",
                "qty": 85,
                "tags": ["gray"],
                "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            },
            {
                "item": "mousepad",
                "qty": 25,
                "tags": ["gel", "blue"],
                "size": {"h": 19, "w": 22.85, "uom": "cm"},
            },
        ]
    )
    print(result)

