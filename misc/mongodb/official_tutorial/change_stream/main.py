from db_conn import mongo_client
from utils import *
from constants import *

with mongo_client(DB) as client:
    watch(client, 'coll_1')
