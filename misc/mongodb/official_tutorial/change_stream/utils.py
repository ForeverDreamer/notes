from pprint import pprint as pp


def watch(client, coll):
    # pipeline = [
    #     {"$match": {"fullDocument.username": "alice"}},
    #     {"$addFields": {"newField": "this is an added field!"}},
    # ]
    # cursor = client.get_default_database()[coll].watch(pipeline=pipeline)
    cursor = client.get_default_database()[coll].watch()
    for doc in cursor:
        print('========================================')
        pp(doc)
