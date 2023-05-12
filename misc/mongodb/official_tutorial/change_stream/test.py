from db_conn import mongo_client
from utils import *
from constants import *

with mongo_client(DB) as client:
    # client.get_default_database()['coll_1'].insert_one({'username': 'alice'})
    # client.get_default_database()['coll_1'].insert_one({'username': 'tom'})
    client.get_default_database()['coll_1'].update_one({'username': 'tom'}, {'$set': {'username': 'alice'}})
