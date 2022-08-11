import contextlib

import pymongo


@contextlib.contextmanager
def mongo_client(uri):
    client = pymongo.MongoClient(uri)
    # print('数据库连接成功！')
    yield client
    client.close()
    # print('关闭数据库！')
