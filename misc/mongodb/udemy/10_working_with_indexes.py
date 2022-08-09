import sys
import random
import math
from pprint import pprint as pp

from pymongo.errors import OperationFailure, DuplicateKeyError
from pymongo import ASCENDING, DESCENDING, TEXT

from db_conn import mongo_client
from utils import utc_now

db_name = 'mongodb_example'


def list_indexes(c):
    pp(list(c.list_indexes()))
    print('--------------------------------------------------')
    pp(c.index_information())


def index_information(c):
    pp(c.index_information())


def drop_index(persons, index):
    try:
        persons.drop_index(index)
        print(f'删除索引<{index}>成功')
    except OperationFailure:
        print(f'索引<{index}>不存在，忽略')


def adding_a_single_field_index_126(persons):
    r = persons.find({'dob.age': {'$gt': 60}}).explain()
    pp(r)
    print('--------------------------------------------')
    r = persons.create_index('dob.age', name='dob.age')
    pp(r)
    print('--------------------------------------------')
    r = persons.find({'dob.age': {'$gt': 60}}).explain()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'dob.age')


def understanding_index_restrictions_128(persons):
    # 返回的数据占比特别高的查询，索引反而会增加查询时间
    # 一般返回的数据占比20%以下，索引能缩短查询时间
    r = persons.create_index('dob.age', name='dob.age')
    pp(r)
    print('--------------------------------------------')
    r = persons.find({'dob.age': {'$gt': 20}}).explain()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'dob.age')
    r = persons.find({'dob.age': {'$gt': 20}}).explain()
    pp(r)
    print('--------------------------------------------')


def creating_compound_indexes_129(persons):
    r = persons.create_index('gender', name='gender')
    pp(r)
    print('--------------------------------------------')
    r = persons.find({'gender': 'male'}).explain()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'gender')
    r = persons.create_index([('dob.age', ASCENDING), ('gender', DESCENDING)], name='dob.age_gender')
    pp(r)
    print('--------------------------------------------')
    # 'stage': 'IXSCAN'
    r = persons.find({'dob.age': 35, 'gender': 'male'}).explain()
    pp(r)
    print('--------------------------------------------')
    # 'stage': 'IXSCAN'
    r = persons.find({'dob.age': 35}).explain()
    pp(r)
    print('--------------------------------------------')
    # 'stage': 'COLLSCAN'
    r = persons.find({'gender': 'male'}).explain()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'dob.age_gender')


# 提升排序速度，且避免数据量太大内存不足排序失败
def using_indexes_for_sorting_130(persons):
    # 无索引的stages: COLLSCAN->SORT
    r = persons.find({'dob.age': 35}).sort('gender', 1).explain()
    pp(r)
    print('--------------------------------------------')
    r = persons.create_index([('dob.age', ASCENDING), ('gender', DESCENDING)], name='dob.age_gender')
    pp(r)
    print('--------------------------------------------')
    # 有索引的stages: IXSCAN->FETCH
    r = persons.find({'dob.age': 35}).sort('gender', 1).explain()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'dob.age_gender')


# 默认索引：{'_id_': {'key': [('_id', 1)], 'v': 2}}
def understanding_the_default_index_131(persons):
    r = persons.create_index('dob.age', name='dob.age')
    pp(r)
    print('--------------------------------------------')
    r = persons.create_index('gender', name='gender')
    pp(r)
    print('--------------------------------------------')
    r = persons.create_index([('dob.age', ASCENDING), ('gender', ASCENDING)], name='dob.age_gender')
    pp(r)
    print('--------------------------------------------')
    r = persons.index_information()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'dob.age')
    drop_index(persons, 'gender')
    drop_index(persons, 'dob.age_gender')


def configuring_indexes_132(persons):
    try:
        persons.create_index('email', name='email', unique=True)
    except DuplicateKeyError as e:
        print(e, file=sys.stderr)
    print('--------------------------------------------')


# 减少索引占用的硬盘空间，新增'female'文档不会更新索引从而提升数据写入速度
def understanding_partial_filters_133(persons):
    r = persons.create_index('dob.age', name='dob.age_gender_male', partialFilterExpression={'gender': 'male'})
    pp(r)
    print('--------------------------------------------')
    # r = persons.create_index('dob.age', name='dob.age_$gt_60', partialFilterExpression={'dob.age': {'$gt': 60}})
    # pp(r)
    # print('--------------------------------------------')
    r = persons.index_information()
    pp(r)
    print('--------------------------------------------')
    # 'stage': 'COLLSCAN'
    r = persons.find({'dob.age': {'$gt': 60}}).explain()
    pp(r)
    print('--------------------------------------------')
    # 'stage': 'IXSCAN'
    r = persons.find({'dob.age': {'$gt': 60}, 'gender': 'male'}).explain()
    pp(r)
    print('--------------------------------------------')
    # 'stage': 'COLLSCAN'
    r = persons.find({'dob.age': {'$gt': 60}, 'gender': 'female'}).explain()
    pp(r)
    print('--------------------------------------------')
    drop_index(persons, 'dob.age_gender_male')


def applying_the_partial_index_134(users):
    users.insert_many([
        {'name': 'Max', 'email': 'max@test.com'},
        {'name': 'Manu'},
    ])
    print(users.create_index('email', name='email'))
    drop_index(users, 'email')
    print(users.create_index('email', name='email', unique=True))
    try:
        users.insert_one({'name': 'Anna'})
    except DuplicateKeyError as e:
        # email dup key: { email: null }
        print(e, file=sys.stderr)
    drop_index(users, 'email')
    print(users.create_index('email', name='email', unique=True, partialFilterExpression={'email': {'$exists': True}}))
    users.insert_one({'name': 'Anna'})
    print('Anna added')
    try:
        users.insert_one({'name': 'Anna', 'email': 'max@test.com'})
    except DuplicateKeyError as e:
        # email dup key: { email: "max@test.com" }
        print(e, file=sys.stderr)
    drop_index(users, 'email')
    users.drop()


def understanding_the_time_to_live_ttl_index_135(sessions):
    # https://docs.mongodb.com/manual/core/index-ttl/
    # The background task that removes expired documents runs every 60 seconds
    sessions.drop()
    sessions.insert_one({'data': '数据', 'time': utc_now()})
    print(sessions.create_index([('time', DESCENDING)], name='time', expireAfterSeconds=3))
    sessions.insert_one({'data': '数据', 'time': utc_now()})
    print('--------------------------------------------')
    pp(sessions.index_information())
    # sessions.drop()


def understanding_covered_queries_137(customers):
    customers.drop()
    customers.insert_many([
        {'name': 'Max', 'age': 29, 'salary': 3000},
        {'name': 'Manu', 'age': 30, 'salary': 4000},
    ])
    print(customers.create_index('name', name='name'))
    pp(customers.find({'name': 'Max'}).explain())
    print('--------------------------------------------')
    # covered query: 从索引就能获取所需数据, 'totalDocsExamined': 0
    pp(customers.find({'name': 'Max'}, {'_id': 0, 'name': 1}).explain())


def how_mongodb_rejects_a_plan_138(customers):
    customers.drop()
    customers.insert_many([
        {'name': 'Max', 'age': 29, 'salary': 3000},
        {'name': 'Manu', 'age': 30, 'salary': 4000},
    ])
    print(customers.create_index('name', name='name'))
    print(customers.create_index([('age', ASCENDING), ('name', ASCENDING)], name='age_name'))
    pp(customers.find({'name': 'Max', 'age': 30}).explain())


def using_multi_key_indexes_139(contacts):
    contacts.drop()
    contacts.insert_one({
        'name': 'Max',
        'hobbies': ['Cooking', 'Sports'],
        'addresses': [
            {'street': 'Main Street'},
            {'street': 'Second Street'},
        ]})
    print('---------------------1-----------------------')
    print(contacts.create_index('hobbies', name='hobbies'))
    pp(contacts.index_information())
    pp(list(contacts.find({'hobbies': 'Sports'})))
    # 'stage': 'IXSCAN', 'isMultiKey': True,
    pp(contacts.find({'hobbies': 'Sports'}).explain())
    print('---------------------2-----------------------')
    print(contacts.create_index('addresses', name='addresses'))
    pp(contacts.index_information())
    # 'stage': 'COLLSCAN'
    pp(contacts.find({'addresses.street': 'Main Street'}).explain()['executionStats'])
    # 'stage': 'IXSCAN', 'isMultiKey': True
    pp(contacts.find({'addresses': {'street': 'Main Street'}}).explain()['executionStats'])
    print('---------------------3-----------------------')
    print(contacts.create_index('addresses.street', name='addresses.street'))
    pp(contacts.index_information())
    # 'stage': 'IXSCAN', 'isMultiKey': True
    pp(contacts.find({'addresses.street': 'Main Street'}).explain()['executionStats'])
    print('---------------------4-----------------------')
    print(contacts.create_index([('name', ASCENDING), ('hobbies', ASCENDING)], name='name_hobbies'))
    pp(contacts.index_information())
    print('---------------------5-----------------------')
    try:
        print(contacts.create_index([('addresses', ASCENDING), ('hobbies', ASCENDING)], name='addresses_hobbies'))
    except OperationFailure as e:
        print(e, file=sys.stderr)


def understanding_text_indexes_140(products):
    products.drop()
    products.insert_many([
        {'title': 'A Book', 'description': 'This is an awesome book about a young artist!'},
        {'title': 'Red T-Shirt', 'description': "This T-Shirt is red and it's pretty awesome!"},
    ])
    print(products.create_index('description', name='description'))
    # 'stage': 'FETCH', 'nReturned': 0, 查不到数据
    pp(products.find({'description': 'awesome book'}).explain()['executionStats'])
    # 完全匹配才能查到
    pp(list(products.find({'description': 'This is an awesome book about a young artist!'})))
    print('--------------------------------------------')
    drop_index(products, 'description')
    # 每个collection只能创建一个text索引
    print(products.create_index([('description', TEXT)], name='description_text', default_language='english'))
    # 'stage': 'TEXT', 'nReturned': 2
    pp(list(products.find({'$text': {'$search': 'awesome'}})))
    print('--------------------------------------------')
    pp(list(products.find({'$text': {'$search': 'book'}})))
    print('--------------------------------------------')
    pp(list(products.find({'$text': {'$search': 'red book'}})))


def text_indexes_sorting_141(products):
    products.drop()
    products.insert_many([
        {'title': 'A Book', 'description': 'This is an awesome book about a young artist!'},
        {'title': 'Red T-Shirt', 'description': "This T-Shirt is red and it's pretty awesome!"},
    ])
    print(products.create_index([('description', TEXT)], name='description_text', default_language='english'))
    pp(list(products.find({'$text': {'$search': 'awesome t-shirt'}})))
    print('--------------------------------------------')
    pp(list(products.find(
        {'$text': {'$search': 'awesome t-shirt'}},
        {'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])))


def creating_combined_text_indexes_142(products):
    products.drop()
    products.insert_many([
        {'title': 'A Book', 'description': 'This is an awesome book about a young artist!'},
        {'title': 'Red T-Shirt', 'description': "This T-Shirt is red and it's pretty awesome!"},
    ])
    print(products.create_index(
        [('title', TEXT), ('description', TEXT)],
        name='title_description_text',
        default_language='english')
    )
    pp(products.index_information())
    print('--------------------------------------------')
    products.insert_one({'title': 'A Ship', 'description': 'Floats perfectly!'})
    pp(list(products.find({'$text': {'$search': 'ship'}})))


def using_text_indexes_to_exclude_words_143(products):
    products.drop()
    products.insert_many([
        {'title': 'A Book', 'description': 'This is an awesome book about a young artist!'},
        {'title': 'Red T-Shirt', 'description': "This T-Shirt is red and it's pretty awesome!"},
    ])
    print(products.create_index(
        [('title', TEXT), ('description', TEXT)],
        name='title_description_text',
        default_language='english')
    )
    pp(list(products.find({'$text': {'$search': 'awesome'}})))
    print('--------------------------------------------')
    # 排除t-shirt
    pp(list(products.find({'$text': {'$search': 'awesome -t-shirt'}})))


def setting_the_default_language_using_weights_144(products):
    products.drop()
    products.insert_many([
        {'title': 'A Book', 'description': 'This is an awesome book about a young artist!'},
        {'title': 'Red T-Shirt', 'description': "This T-Shirt is red and it's pretty awesome!"},
    ])
    print(products.create_index(
        [('title', TEXT), ('description', TEXT)],
        name='title_description_text',
        default_language='english',
        weights={'title': 1, 'description': 10})
    )
    pp(products.index_information())
    print('--------------------------------------------')
    pp(list(products.find({'$text': {'$search': 't-shirt', '$caseSensitive': True}})))
    print('--------------------------------------------')
    # 默认大小写不敏感
    pp(list(products.find({'$text': {'$search': 't-shirt'}})))
    print('--------------------------------------------')
    # 指定weights, score大幅提升
    pp(list(products.find(
        {'$text': {'$search': 'red'}},
        {'score': {'$meta': 'textScore'}})))


def building_indexes_145(ratings):
    ratings.drop()
    # count = 1000000
    count = 100
    for i in range(count):
        ratings.insert_one({
            'person_id': i + 1,
            'score': random.random() * 100,
            'age': math.floor(random.random() * 70) + 18,
        })
    # 开发环境用Foreground: 阻塞collection访问，创建速度快
    ratings.create_index('age', name='age')
    # stage: IXSCAN
    pp(ratings.find({'age': {'$gt': 80}}).explain()['executionStats'])
    print('--------------------------------------------')
    drop_index(ratings, 'age')
    # stage: COLLSCAN
    pp(ratings.find({'age': {'$gt': 80}}).explain()['executionStats'])
    print('--------------------------------------------')
    # 生产环境用Background: 允许collection访问，创建速度慢
    ratings.create_index('age', name='age', background=True)
    pp(ratings.index_information())


with mongo_client(db_name) as client:
    col = client.get_default_database()['persons']
    # list_indexes(col)
    # adding_a_single_field_index_126(col)
    # understanding_index_restrictions_128(col)
    # creating_compound_indexes_129(col)
    using_indexes_for_sorting_130(col)
    # understanding_the_default_index_131(col)
    # configuring_indexes_132(col)
    # understanding_partial_filters_133(col)
    # applying_the_partial_index_134(client.get_default_database()['users'])
    # understanding_the_time_to_live_ttl_index_135(client.get_default_database()['sessions'])
    # understanding_covered_queries_137(client.get_default_database()['customers'])
    # how_mongodb_rejects_a_plan_138(client.get_default_database()['customers'])
    # using_multi_key_indexes_139(client.get_default_database()['contacts'])
    # understanding_text_indexes_140(client.get_default_database()['products'])
    # text_indexes_sorting_141(client.get_default_database()['products'])
    # creating_combined_text_indexes_142(client.get_default_database()['products'])
    # using_text_indexes_to_exclude_words_143(client.get_default_database()['products'])
    # setting_the_default_language_using_weights_144(client.get_default_database()['products'])
    # building_indexes_145(client.get_default_database()['ratings'])
