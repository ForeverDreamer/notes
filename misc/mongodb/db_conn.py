import contextlib

import pymongo


@contextlib.contextmanager
def mongo_client(d):
    client = pymongo.MongoClient(f'mongodb://root:Root%401234.@192.168.71.20:9302/{d}?authSource=admin')
    # print('数据库连接成功！')
    yield client
    client.close()
    # print('关闭数据库！')
