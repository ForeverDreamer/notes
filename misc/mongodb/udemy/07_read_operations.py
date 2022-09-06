from pprint import pprint as pp
import json

from pymongo.errors import BulkWriteError
from pymongo.write_concern import WriteConcern

from db_conn import mongo_client
from utils import utc_now

db_name = 'mongodb_example'


def init_db():
    with mongo_client(db_name) as client:
        # client.drop_database(db_name)
        d = client.get_default_database()
        with open('078-tv-shows.json', 'rb') as f:
            movies = json.load(f)
        d['movies'].insert_many(movies)


# init_db()


def understanding_findone_find_081():
    doc = coll.find_one({'runtime': 60})
    pp(doc)
    print('--------------------------------------------------')
    cursor = coll.find({})
    for doc in cursor:
        pp(doc)
        break


with mongo_client(db_name) as client:
    coll = client.get_default_database()['movies']
    understanding_findone_find_081()