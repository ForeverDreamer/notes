import json
from pprint import pprint as pp

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
pp(es.info())
# es = Elasticsearch()


# Indices

# Creates an index with optional settings and mappings
# res = es.indices.create(index='customers')

# Deletes an index
# res = es.indices.delete(index=['customers'])

# Returns information about whether a particular index exists
# res = es.indices.exists(index=['customers'])

# Returns information about one or more indices
# res = es.indices.get(index=['customers'])

# Returns mappings for one or more indices
# res = es.indices.get_mapping(index=['news'])

# Updates the index mappings
# res = es.indices.put_mapping(body={}, index=['news'])

# Returns settings for one or more indices
# res = es.indices.get_settings(index=['customers'])

# Updates the index settings
# res = es.indices.put_settings(body={}, index=['news'])

# Provides statistics on operations happening in an index
# res = es.indices.stats(index=['customers'])


# Cat

# Returns information about indices: number of primaries and replicas, document counts, disk
# res = es.cat.indices(params={'v': 'true'})
# res = es.cat.indices(index=['customers'], params={'v': 'true'})

# Provides quick access to the document count of the entire cluster, or individual indices
# res = es.cat.count(params={'v': 'true'})

# Returns information about existing templates
# res = es.cat.templates(params={'v': 'true'})


# Elasticsearch

# Creates a new document in the index, 不好用，尽量使用es.index()
# body = {"name": "Michael Sharpe", "age": 22, "gender": "male", "email": "michaelsharpe@talkalot.com",
#         "phone": "+1 (942) 544-2868", "street": "858 Bushwick Court", "city": "Dorneyville",
#         "state": "American Samoa, 3711"}
# res = es.create(index='customers', id=1, body=body)

# Returns information about whether a document exists in an index
# res = es.exists(index='customers', id=1)

# Returns information about whether a document source exists in an index
# res = es.exists_source(index='customers', id=1)

# Returns a document
# res = es.get(index='customers', id=1)

# Removes a document from the index.
# res = es.delete(index='customers', id=1)

# Returns number of documents matching a query
# res = es.count()

# Returns information about why a specific matches (or doesn’t match) a query
# body = {
#     'query': {
#         'match': {
#             'name': 'Sharpe'
#         }
#     }
# }
# res = es.explain(index='customers', id=1, body=body)

# Returns the source of a document
# res = es.get_source(index='customers', id=1)

# Creates or updates a document in an index
# body = {"name": "Michael Sharpe", "age": 22, "gender": "male", "email": "michaelsharpe@talkalot.com",
#         "phone": "+1 (942) 544-2868", "street": "858 Bushwick Court", "city": "Dorneyville",
#         "state": "American Samoa, 3711"}
# res = es.index(index='customers', body=body, id=1)

# Allows to get multiple documents in one request
# body = {
#   "docs": [
#     {
#       "_index": "customers",
#       "_id": "1"
#     },
#     {
#       "_index": "customers",
#       "_id": "2"
#     }
#   ]
# }
# res = es.mget(body=body, index='customers')

# Allows to execute several search operations in one request
# search_arr = [
#     {},
#     {"query": {"match_all": {}}, "from": 0, "size": 10},
#     {},
#     {"query": {"match_all": {}}},
#     {"index": "customers"},
#     {"query": {"match_all": {}}},
# ]
#
# body = ''
# for each in search_arr:
#     body += f'{json.dumps(each)}\n'
#
# res = es.msearch(body=body)

# Returns whether the cluster is running
# res = es.ping()

# Allows to copy documents from one index to another, optionally filtering the source documents by a query,
# changing the destination index settings, or fetching the documents from a remote cluster
# body = {
#   "source": {
#     "index": "customers"
#   },
#   "dest": {
#     "index": "customers_reindex"
#   }
# }
# res = es.reindex(body=body)

# Returns results matching a query
# body = {
#     'query': {
#         'match': {
#             'name': 'Sharpe'
#         }
#     }
# }
# res = es.search(body=body)

# Allows to retrieve a large numbers of results from a single search request
# body = {
#     "size": 10,
#     "query": {"match_all": {}},
#     "sort": [
#         {"age": "asc"},
#         {"c_id": "asc"}
#     ]
# }
# res = es.search(
#     index=['customers', 'customers_reindex'],
#     # index=['news'],
#     body=body,
# )
#
# for i in range(10):
#     body = {
#         "size": 10,
#         "query": {"match_all": {}},
#         "search_after": res['hits']['hits'][9]['sort'],
#         "sort": [
#             {"age": "asc"},
#             {"c_id": "asc"}
#         ]
#     }
#     res = es.search(
#         index=['customers', 'customers_reindex'],
#         # index=['news'],
#         body=body,
#     )
#     pp(body['search_after'])

# body = {
#     "size": 10,
#     "query": {"match_all": {}},
# }
# res = es.search(
#     index=['news'],
#     body=body,
# )

# res = es.indices.get_mapping(index=['news'])
# res = es.count(index=['news'])

# body = {
#     "size": 10,
#     "query": {"match_all": {}},
#     "sort": [
#         {"view": "desc"},
#         {'_id': "asc"}
#     ]
# }
# res = es.search(
#     index=['news'],
#     body=body,
# )

# for i in range(10):
#     r_size = len(res['hits']['hits'])
#     if r_size == 0:
#         break
#     search_after = res['hits']['hits'][-1]['sort']
#     body = {
#         "size": 1,
#         "query": {"match_all": {}},
#         "search_after": search_after,
#         "sort": [
#             {"crawler.date": "desc"},
#             {'id': "desc"}
#         ]
#     }
#     res = es.search(
#         index=['news'],
#         body=body,
#     )
#     pp(body['search_after'])
#     pp([
#         (hit['_source']['crawler']['date'], hit['_source']['translator']['zh-CN']['title'])
#         for hit in
#         res['hits']['hits']
#     ])
#     print()

# res = es.update(index="news", id='5f9b4f259dc6d63e8818bb59', body={"doc": {"view": 100}})

# pp(res)
