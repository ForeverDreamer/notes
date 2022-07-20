import contextlib

import pymongo


@contextlib.contextmanager
def mongo_client(d):
    client = pymongo.MongoClient(f'mongodb://root:PassForCfe123@localhost:27017/{d}?authSource=admin')
    # print('数据库连接成功！')
    yield client
    client.close()
    # print('关闭数据库！')
