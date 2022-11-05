import contextlib
import sys

import pymongo


@contextlib.contextmanager
def mongo_client(d):
    # <ENTER>
    # client = pymongo.MongoClient(f'mongodb://root:PassForCfe123@192.168.80.129:27017/{d}?authSource=admin')
    client = pymongo.MongoClient(f'mongodb://mongo1:27021,mongo2:27022,mongo3:27023/{d}?replicaSet=dbrs')
    # print('数据库连接成功！')
    try:
        # Like __enter__()'s return statement
        yield client
        # <NORMAL EXIT>
        client.close()
        # print('关闭数据库！')
    except Exception:
        # <EXCEPTIONAL EXIT>
        # print('mongo_client: exceptional exit', sys.exc_info())
        raise

