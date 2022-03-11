import json
from pprint import pprint as pp

from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch()
# pp(es.info())
# pp(es.cluster.health())

# with open('customers_full.txt', 'rt') as f:
#     c_id = 1
#     for line in f.readlines():
#         if line.strip() == '{"index" : {}}':
#             continue
#         else:
#             doc = json.loads(line.strip())
#             doc['c_id'] = c_id
#             res = es.index(index='customers', body=doc)
#             if c_id % 100 == 0:
#                 print('=============================================================')
#                 print(res)
#             c_id += 1

# with open("customers_full.txt", "r") as f1:
#     lines = f1.readlines()
#     with open("customers_full(modified).txt", "w") as f2:
#         for line in lines:
#             if line.strip() != '{"index" : {}}':
#                 f2.write(line)


# def gen_customer_data():
#     with open("customers_full(modified).txt", "r") as f:
#         i = 1
#         for doc in f.readlines():
#             yield {
#                 '_op_type': 'create',
#                 '_index': 'customers',
#                 '_id': i,
#                 '_source': json.loads(doc.strip())
#             }
#             i += 1
#
#
# pp(helpers.bulk(es, gen_customer_data()))

# Searching and Analyzing Data with Elasticsearch: Getting Started


# 3.Executing CRUD Operations Using the Elasticsearch APIs
# 1)Introducing the cURL Command Line Utility
# print(es.cat.indices(params={'v': 'true'}))
print(es.cat.nodes(params={'v': 'true'}))

# 2)Creating Indices
# print(es.indices.create(index='products'))
# print(es.indices.create(index='customers'))
# print(es.indices.create(index='orders'))

# 3)Adding Documents to an Index
# pp(es.create(index='customers',
#              id=1,
#              body={"name": "Michael Sharpe", "age": 22, "gender": "male", "email": "michaelsharpe@talkalot.com",
#                    "phone": "+1 (942) 544-2868", "street": "858 Bushwick Court", "city": "Dorneyville",
#                    "state": "American Samoa, 3711"}))
# pp(es.create(index='customers',
#              id=2,
#              body={"name": "Abigail Garcia", "age": 31, "gender": "female", "email": "abigailgarcia@talkalot.com",
#                    "phone": "+1 (928) 499-3611", "street": "114 Bulwer Place", "city": "Wyano", "state": "Utah, 118"}))
# pp(es.create(index='customers',
#              id=3,
#              body={"name": "Harris Hebert", "age": 47, "gender": "male", "email": "harrishebert@talkalot.com",
#                    "phone": "+1 (851) 589-3367", "street": "907 Hoyts Lane", "city": "Bartonsville",
#                    "state": "North Dakota, 5506"}))

# 4)Retrieving Whole and Partial Documents
# pp(es.get(index='customers', id=2))
# pp(es.get_source(index='customers', id=1))
# pp(es.get(index='customers', id=2, _source_includes=['name', 'age', 'phone']))
# pp(es.get(index='customers', id=3, _source=False))

# 5)Updating Whole and Partial Documents
# 指定id已存在则更新文档（body内容替换覆盖旧文档），不存在则新建文档；如不指定id则新建文档，自动生成id（即使body内容一模一样）
# pp(es.index(index='customers', id='5GU8rXoBMpZykDqfN-jr',
#             body={"name": "lishenglin", "age": 22}))
# pp(es.index(index='customers', id='3',
#             body={"name": "lishenglin", "age": 22}))
# pp(es.index(index='customers',
#             body={"name": "lishenglin", "age": 22}))

# 部分更新文档，字段存在则更新value，字段不存在则创建（已有字段不受影响）；如果body一模一样则不会更新文档；
# pp(es.update(index='customers', id='2', body={'doc': {"gender": "female", "email": "123456@qq.com"}}))
# pp(es.update(index='customers', id='3', body={'doc': {"name": "doer"}}))
# pp(es.update(index='customers', id='3', body={"script": "ctx._source.age += 1"}))

# 6)Deleting Documents and Indices
# pp(es.delete(index='customers', id=3))
# pp(es.delete_by_query(index='customers', body={'query': {'match_all': {}}}))
# pp(es.indices.delete(index='customers'))
# pp(es.indices.delete(index='_all'))  # index='*'


# 7)Performing Bulk Operations on Documents
# pp(es.mget(index='customers', body=({'ids': [1, 2, 3]})))
# pp(es.mget(body=({'docs': [
#     {'_index': 'customers', '_id': 1},
#     {'_index': 'customers', '_id': 2},
#     {'_index': 'customers', '_id': 3}]})))
# pp(es.mget(index='customers', body=({'docs': [
#     {'_id': 1},
#     {'_id': 2},
#     {'_id': 3}]})))


# def gen_create_data():
#     docs = [{"name": "Michael Sharpe", "age": 22, "gender": "male", "email": "michaelsharpe@talkalot.com",
#              "phone": "+1 (942) 544-2868", "street": "858 Bushwick Court", "city": "Dorneyville",
#              "state": "American Samoa, 3711"},
#             {"name": "Abigail Garcia", "age": 31, "gender": "female", "email": "abigailgarcia@talkalot.com",
#              "phone": "+1 (928) 499-3611", "street": "114 Bulwer Place", "city": "Wyano", "state": "Utah, 118"},
#             {"name": "Harris Hebert", "age": 47, "gender": "male", "email": "harrishebert@talkalot.com",
#              "phone": "+1 (851) 589-3367", "street": "907 Hoyts Lane", "city": "Bartonsville",
#              "state": "North Dakota, 5506"}
#             ]
#     i = 1
#     for doc in docs:
#         yield {
#             '_op_type': 'create',
#             '_index': 'customers',
#             '_id': i,
#             '_source': doc
#         }
#         i += 1
#
#
# def gen_index_data():
#     docs = [
#         {"name": "lsl1", "age": 20},
#         {"name": "lsl2", "age": 21},
#         {"name": "lsl3", "age": 22},
#     ]
#     i = 1
#     for doc in docs:
#         yield {
#             '_op_type': 'index',
#             '_index': 'customers',
#             '_id': i,
#             '_source': doc
#         }
#         i += 1
#
#
# def gen_update_data():
#     for i in range(3):
#         yield {
#             '_op_type': 'update',
#             '_index': 'customers',
#             '_id': i+1,
#             'doc': {'question': 'The life, universe and everything.'}
#         }
#
#
# def gen_delete_data():
#     for i in range(3):
#         yield {
#             '_op_type': 'delete',
#             '_index': 'customers',
#             '_id': i+1,
#         }


# pp(helpers.bulk(es, gen_create_data()))
# pp(helpers.bulk(es, gen_index_data()))
# pp(helpers.bulk(es, gen_update_data()))
# pp(helpers.bulk(es, gen_delete_data()))


# 4 Executing Search Requests Using Elasticsearch Query DSL
# 5)Search Using the Request Body
# body = {
#     'query': {'match_all': {}},
# }
# body = {
#     'query': {'match_all': {}},
#     'from': 10,
#     'size': 20,
#     'sort': {'age': {'order': 'desc'}}
# }

# 6)Source Filtering Document Contents
# Term query
# Returns documents that contain an exact term in a provided field.
# You can use the term query to find documents based on a precise value such as a price, a product ID, or a username
# body = {
#     'query': {'term': {'name': 'gates'}},
# }

# body = {
#     'query': {'term': {'street': 'chestnut'}},
# }

# 不返回_source字段
# body = {
#     '_source': False,
#     'query': {'term': {'street': 'chestnut'}},
# }

# 只返回'_source'字段中以'st'开头或包括'n'的字段
# body = {
#     '_source': 'st*',
#     'query': {'term': {'state': 'washington'}},
# }

# body = {
#     '_source': ['st*', '*n*'],
#     'query': {'term': {'state': 'washington'}},
# }

# body = {
#     '_source': {
#         'includes': ['st*', '*n*'],
#         'excludes': ['*der']
#     },
#     'query': {'term': {'state': 'washington'}},
# }

# 7)Full Text Searchs
# body = {
#     'query': {
#         'match': {
#             'name': 'webster'
#         }
#     }
# }

# 包含frank或norris的文档，不指定operator默认为or
# body = {
#     'query': {
#         'match': {
#             'name': {
#                 'query': 'frank norris',
#                 'operator': 'or'
#             }
#         }
#     }
# }

# 不指定operator默认为or
# body = {
#     'query': {
#         'match': {
#             'street': 'tompkins place'
#         }
#     }
# }

# body = {
#     'query': {
#         'match_phrase': {
#             'street': 'tompkins place',
#             # 'state': 'puerto rico'
#         }
#     }
# }

# body = {
#     'query': {
#         'match_phrase_prefix': {
#             'name': 'ma',
#             # 'street': 'clymer st'
#         }
#     }
# }

# 9)Queries with Common Terms(7.3之后已弃用，使用match就好)
# body = {
#     'query': {
#         'common': {
#             'reviews': {
#                 'query': 'this is great',
#                 'cutoff_frequency': 0.001
#             }
#         }
#     }
# }

# 10)Boolean Compound Queries
# body = {
#     'query': {
#         'bool': {
#             'must': [
#                 {'match': {'street': 'ditmas'}},
#                 {'match': {'street': 'avenue'}}
#             ]
#         }
#     }
# }

# body = {
#     'query': {
#         'bool': {
#             'should': [
#                 {'match': {'street': 'ditmas'}},
#                 {'match': {'street': 'street'}}
#             ]
#         }
#     }
# }

# body = {
#     'query': {
#         'bool': {
#             'must_not': [
#                 {'match': {'state': 'california texas'}},
#                 {'match': {'street': 'lane street'}}
#             ]
#         }
#     }
# }

# 11)Term Queries and the Boost Parameter
# body = {
#     'query': {
#         'bool': {
#             'should': [
#                 {
#                     'term': {
#                             'state': {
#                                 'value': 'idaho',
#                                 'boost': 2.0
#                             }
#                     }
#                 },
#                 {
#                     'term': {
#                         'state': {
#                             'value': 'california'
#                         }
#                     }
#                 },
#             ]
#         }
#     }
# }

# 12)Search Using the Filter Context
# body = {
#     'query': {
#         'bool': {
#             'must': {'match_all': {}},
#             'filter': {
#                 'range': {
#                     'age': {
#                         'gte': 20,
#                         'lte': 30,
#                     }
#                 }
#             }
#         }
#     }
# }

# body = {
#     'query': {
#         'bool': {
#             'must': {
#                 'match': {
#                     'state': 'alabama',
#                 }
#             },
#             'filter': [
#                 {'term': {'gender': 'female'}},
#                 {'range': {'age': {'gte': 50}}}
#             ]
#         }
#     }
# }


# 5 Executing Analytical Queries Through Aggregations
# 2)Implementing Metric Aggregations
# body = {
#     'size': 0,
#     # 'aggregations': {
#     'aggs': {
#         'avg_age': {
#             'avg': {
#                 'field': 'age'
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'query': {
#         'bool': {
#             'filter': {
#                 'match': {'state': 'minnesota'}
#             }
#         }
#     },
#     'aggs': {
#         'avg_age': {
#             'avg': {
#                 'field': 'age'
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'aggs': {
#         'age_stats': {
#             'stats': {
#                 'field': 'age'
#             }
#         }
#     }
# }

# 3)The Cardinality Aggregation

# Enable fielddata for text fields via mappings
# curl -XPUT 'localhost:9200/customers/_mapping/personal?pretty' -H 'Content-Type: application/json' -d'{"properties": {"gender": {"type": "text", "fielddata": true}}}'

# body = {
#     'size': 0,
#     'aggs': {
#         # 'age_count': {
#         #     'cardinality': {
#         #         'field': 'age'
#         #     }
#         # }
#         'gender_count': {
#             'cardinality': {
#                 'field': 'gender'
#             }
#         }
#     }
# }

# 4)Implementing Bucketing Aggregations
# body = {
#     'size': 0,
#     'aggs': {
#         'gender_bucket': {
#             'terms': {
#                 'field': 'gender'
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'aggs': {
#         'age_bucket': {
#             'terms': {
#                 'field': 'age'
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'aggs': {
#         'age_ranges': {
#             'range': {
#                 'field': 'age',
#                 # 'keyed': True,
#                 'ranges': [
#                     {'to': 30},
#                     {'from': 30, 'to': 40},
#                     {'from': 40, 'to': 50},
#                     {'from': 55},
#                 ]
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'aggs': {
#         'age_ranges': {
#             'range': {
#                 'field': 'age',
#                 'keyed': True,
#                 'ranges': [
#                     {'key': 'young', 'to': 30},
#                     {'key': 'quarter-aged', 'from': 30, 'to': 40},
#                     {'key': 'middle-aged', 'from': 40, 'to': 50},
#                     {'key': 'senior', 'from': 55},
#                 ]
#             }
#         }
#     }
# }

# 5)Muti-level Nested Aggregations
# body = {
#     'size': 0,
#     'aggs': {
#         'gender_bucket': {
#             'terms': {
#                 'field': 'gender'
#             },
#             'aggs': {
#                 'average_age': {
#                     'avg': {
#                         'field': 'age'
#                     }
#                 }
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'aggs': {
#         'gender_bucket': {
#             'terms': {
#                 'field': 'gender'
#             },
#             'aggs': {
#                 'age_ranges': {
#                     'range': {
#                         'field': 'age',
#                         'keyed': True,
#                         'ranges': [
#                             {'key': 'young', 'to': 30},
#                             {'key': 'middle-aged', 'from': 30, 'to': 55},
#                             {'key': 'senior', 'from': 55},
#                         ]
#                     },
#                     'aggs': {
#                         'average_age': {
#                             'avg': {
#                                 'field': 'age'
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }

# 6)The Filter and Filters Bucketing Aggregations
# body = {
#     'aggs': {
#         'state': {
#             'filter': {'term': {'state': 'texas'}},
#             'aggs': {
#                 'avg_age': {'avg': {'field': 'age'}}
#             }
#         }
#     }
# }

# body = {
#     'size': 0,
#     'aggs': {
#         'states': {
#             'filters': {
#                 'filters': {
#                     'washington': {'match': {'state': 'washington'}},
#                     'north carolina': {'match': {'state': 'north carolina'}},
#                     'south dakota': {'match': {'state': 'south dakota'}},
#                 }
#             }
#         }
#     }
# }


# Indexing Data in Elasticsearch


# res = es.search(
#     index=['customers'],
#     body=body
# )
# hits = res['hits']['hits']
# pp(res)
