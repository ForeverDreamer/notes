from pprint import pprint as pp

from pymongo.errors import BulkWriteError
from pymongo.write_concern import WriteConcern

from db_conn import mongo_client
from utils import utc_now

db_name = 'mongodb_example'


def understanding_insert_methods_069():
    r = coll.insert_one({'name': 'Max', 'age': 30, 'hobbies': ['Sports', 'Cooking']})
    pp(r.inserted_id)
    print('--------------------------------------------------')
    r = coll.insert_many([
        {'name': 'Anna', 'age': 29, 'hobbies': ['Sports', 'Yoga']},
        {'name': 'Maria', 'age': 31},
        {'name': 'Chris', 'hobbies': ["do nothing"]}
    ])
    pp(r.inserted_ids)


def working_with_ordered_inserts_070():
    r = coll.insert_many([
        {'_id': 'sports', 'name': 'Sports'},
        {'_id': 'cooking', 'name': 'Cooking'},
        {'_id': 'cars', 'name': 'Cars'}
    ])
    pp(r.inserted_ids)
    print('--------------------------------------------------')
    # ordered: 批量插入时按顺序插入，遇到错误立即终止，默认为true
    # pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 1, 'code': 11000,
    # 'keyPattern': {'_id': 1}, 'keyValue': {'_id': 'cooking'}, 'errmsg': 'E11000 duplicate key error collection:
    # mongodb_example.hobbies index: _id_ dup key: { _id: "cooking" }', 'op': {'_id': 'cooking', 'name': 'Cooking'}}],
    # 'writeConcernErrors': [], 'nInserted': 1, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0,
    # 'upserted': []}
    # r = coll.insert_many([
    #     {'_id': 'yoga', 'name': 'Yoga'},
    #     {'_id': 'cooking', 'name': 'Cooking'},
    #     {'_id': 'hiking', 'name': 'Hiking'}
    # ])
    # pp(r.inserted_ids)
    print('--------------------------------------------------')
    # ordered设置为false则会处理所有的数据并返回处理结果；已插入的数据均不会回滚撤销
    try:
        r = coll.insert_many([
            {'_id': 'yoga', 'name': 'Yoga'},
            {'_id': 'cooking', 'name': 'Cooking'},
            {'_id': 'hiking', 'name': 'Hiking'}
        ], ordered=False)
        pp(r.inserted_ids)
    except BulkWriteError as e:
        print(e)


# https://pymongo.readthedocs.io/en/stable/api/pymongo/write_concern.html#pymongo.write_concern.WriteConcern
# writeConcern: w写入实例的数量，默认1， w=<integer> always includes the replica set primary (e.g. w=3 means write to the primary
# and wait until replicated to two secondaries), j表示是否写入journal确保db服务器挂掉内存数据丢失，重启后依然可以根据journal
# 继续未完成的写操作, wtimeout表示超时设置, fsync: If True and the server is running without journaling, blocks until the
# server has synced all data files to disk.
def the_writeconcern_in_practice_072():
    r = coll.with_options(
        write_concern=WriteConcern(w=1, j=True, wtimeout=200)
    ).insert_one({'name': 'Aliya', 'age': 22})
    print(r.acknowledged, r.inserted_id)
    print('--------------------------------------------------')
    # 速度最快，不需要等待执行结果
    r = coll.with_options(
        write_concern=WriteConcern(w=0)
    ).insert_one({'name': 'Aliya', 'age': 22})
    print(r.acknowledged, r.inserted_id)


with mongo_client(db_name) as client:
    coll = client.get_default_database()['people']
    # understanding_insert_methods_069()
    # coll = client.get_default_database()['hobbies']
    # working_with_ordered_inserts_070()
    the_writeconcern_in_practice_072()
