import os
from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()
index_name = 'my-index-000001'
# print(es.cat.indices(params={'v': 'true'}))
# pp(delete_index(es, 'my-index-000001'))

# Collapse search results
# pp(create_index(es, 'my-index-000001', {
#     'mappings': {
#         'properties': {
#             '@timestamp': {'type': 'date'},
#             'geo': {
#                 'properties': {
#                     'country_name': {'type': 'keyword'}
#                 }
#             },
#             'http': {
#                 'properties': {
#                     'request': {
#                         'properties': {
#                             'method': {'type': 'keyword'}
#                         }
#                     },
#                     'response': {
#                         'properties': {
#                             'bytes': {'type': 'integer'},
#                             'status_code': {'type': 'short'}
#                         }
#                     },
#                     'version': {'type': 'keyword'}
#                 }
#             },
#             'message': {'type': 'text'},
#             'source': {
#                 'properties': {
#                     'ip': {'type': 'ip'}
#                 }
#             },
#             'user': {
#                 'properties': {
#                     'id': {'type': 'keyword'}
#                 }
#             }
#         }
#     }
# }))

# pp(get_mapping(es, 'my-index-000001'))

# users = ['Mike', 'John', 'David', 'Tom', 'charles', 'kimchy']
# countries = ['Amsterdam', 'China', 'America', 'Japan', 'British', 'Korea']
#
# doc_id = 1
# for user in users:
#     for country in countries:
#         pp(add_document(es, 'my-index-000001', doc_id, {
#             "@timestamp": f"{2000+doc_id}-11-15T14:12:12",
#             "geo": {
#                 "country_name": country
#             },
#             "http": {
#                 "request": {
#                     "method": "get"
#                 },
#                 "response": {
#                     "bytes": 1070000+doc_id*10,
#                     "status_code": 200
#                 },
#                 "version": "1.1"
#             },
#             "message": f"GET /search HTTP/1.1 200 {1070000+doc_id*10}",
#             "source": {
#                 "ip": "127.0.0.1"
#             },
#             "user": {
#                 "id": user
#             }
#         }))
#         doc_id += 1


# res = search_document(es, 'my-index-000001', {
#     "query": {
#         "match": {
#             "message": "GET /search"
#         }
#     },
#     "collapse": {
#         "field": "user.id"
#     },
#     "sort": [
#         {
#             "http.response.bytes": {
#                 "order": "desc"
#             }
#         }
#     ],
#     "from": 0
# })

# res = search_document(es, 'my-index-000001', {
#     "query": {
#         "match": {
#             "message": "GET /search"
#         }
#     },
#     "collapse": {
#         "field": "user.id",
#         "inner_hits": {
#             "name": "most_recent",
#             "size": 5,
#             "sort": [{"@timestamp": "desc"}]
#         },
#         "max_concurrent_group_searches": 4
#     },
#     "sort": [
#         {
#             "http.response.bytes": {
#                 "order": "desc"
#             }
#         }
#     ]
# })

# res = search_document(es, 'my-index-000001', {
#     "query": {
#         "match": {
#             "message": "GET /search"
#         }
#     },
#     "collapse": {
#         "field": "user.id",
#         "inner_hits": [
#             {
#                 "name": "largest_responses",
#                 "size": 3,
#                 "sort": [
#                     {
#                         "http.response.bytes": {
#                             "order": "desc"
#                         }
#                     }
#                 ]
#             },
#             {
#                 "name": "most_recent",
#                 "size": 3,
#                 "sort": [
#                     {
#                         "@timestamp": {
#                             "order": "desc"
#                         }
#                     }
#                 ]
#             }
#         ]
#     },
#     "sort": [
#         "http.response.bytes"
#     ]
# })

# res = search_document(es, 'my-index-000001', {
#     "query": {
#         "match": {
#             "message": "GET /search"
#         }
#     },
#     "collapse": {
#         "field": "user.id"
#     },
#     "sort": ["user.id"],
#     "search_after": ["dd5ce1ad"]
# })

# res = search_document(es, 'my-index-000001', {
#     "query": {
#         "match": {
#             "message": "GET /search"
#         }
#     },
#     "collapse": {
#         "field": "geo.country_name",
#         "inner_hits": {
#             "name": "by_location",
#             "collapse": {"field": "user.id"},
#             "size": 3
#         }
#     }
# })


# Filter search results
# pp(delete_index(es, index_name))
# res = create_index(es, index_name, {
#     "mappings": {
#         "properties": {
#             "brand": {"type": "keyword"},
#             "color": {"type": "keyword"},
#             "model": {"type": "keyword"}
#         }
#     }
# })

# brands = ['gucci', 'prada', 'nike', 'adidas', 'selected']
# colors = ['red', 'green', 'blue', 'purple', 'yellow']
# models = ['slim', 'normal', 'fat']
#
# doc_id = 1
# for brand in brands:
#     for color in colors:
#         for model in models:
#             pp(add_document(es, index_name, doc_id, {
#                 "brand": brand,
#                 "color": color,
#                 "model": model
#             }))
#             doc_id += 1


# res = search_document(es, index_name, {
#     "query": {
#         "bool": {
#             "filter": [
#                 {"term": {"color": "red"}},
#                 {"term": {"brand": "gucci"}}
#             ]
#         }
#     }
# })

# res = search_document(es, index_name, {
#     "query": {
#         "bool": {
#             "filter": [
#                 {"term": {"color": "red"}},
#                 {"term": {"brand": "gucci"}}
#             ]
#         }
#     },
#     "aggs": {
#         "models": {
#             "terms": {"field": "model"}
#         }
#     }
# })

# res = search_document(es, index_name, {
#     "query": {
#         "bool": {
#             "filter": {
#                 "term": {"brand": "gucci"}
#             }
#         }
#     },
#     "aggs": {
#         "colors": {
#             "terms": {"field": "color"}
#         },
#         "color_red": {
#             "filter": {
#                 "term": {"color": "red"}
#             },
#             "aggs": {
#                 "models": {
#                     "terms": {"field": "model"}
#                 }
#             }
#         }
#     },
#     "post_filter": {
#         "term": {"color": "red"}
#     }
# })


# Paginate search results
# res = search_document(es, index_name, {
#     "from": 1,
#     "size": 3,
#     "query": {
#         "term": {
#             "user.id": "kimchy"
#         }
#     }
# })

# pit_id_file = 'pit_id.txt'

# pit_id = es.open_point_in_time(index=index_name, params={'keep_alive': '1m'})['id']
# with open(pit_id_file, "w", encoding='utf-8') as f:
#     f.write(pit_id)

# with open(pit_id_file, "rt", encoding='utf-8') as f:
#     pit_id = f.readline()

# res = search_document(es, None, {
#     "size": 2,
#     "query": {
#         "match": {
#             "user.id": "John"
#         }
#     },
#     "pit": {
#         "id": pit_id,
#         "keep_alive": "1m"  # 每次请求有效期都会重置为1分钟,1分钟之内一个请求都没有pit才会过期
#     },
#     "sort": [
#         {"@timestamp": {"order": "asc", "format": "strict_date_optional_time_nanos", "numeric_type": "date_nanos"}},
#         # {"_shard_doc": "desc"}  # 可以忽略, 默认自动添加
#     ]
# })

# res = search_document(es, None, {
#     "size": 2,
#     "query": {
#         "match": {
#             "user.id": "John"
#         }
#     },
#     "pit": {
#         "id": pit_id,
#         "keep_alive": "1m"
#     },
#     "sort": [
#         {"@timestamp": {"order": "asc", "format": "strict_date_optional_time_nanos"}}
#     ],
#     "search_after": ['2010-11-15T14:12:12.000Z', 9],
#     "track_total_hits": False
# })

# res = es.close_point_in_time(body={'id': pit_id})


# Retrieve selected fields from a search
# pp(search_document(es, index_name, {
#     "query": {
#         "match": {
#             "user.id": "kimchy"
#         }
#     },
#     "fields": [
#         "user.id",
#         "http.response.*",
#         {
#             "field": "@timestamp",
#             "format": "epoch_millis"
#         }
#     ],
#     "_source": False
# }))

# pp(create_index(es, index_name, {
#     "mappings": {
#         "properties": {
#             "group": {"type": "keyword"},
#             "user": {
#                 "type": "nested",
#                 "properties": {
#                     "first": {"type": "keyword"},
#                     "last": {"type": "keyword"}
#                 }
#             }
#         }
#     }
# }))

# pp(es.index(index=index_name, id='1', params={'refresh': 'true'}, body={
#     "group": "fans",
#     "user": [
#         {
#             "first": "John",
#             "last": "Smith"
#         },
#         {
#             "first": "Alice",
#             "last": "White"
#         }
#     ]
# }))

# pp(search_document(es, index_name, {
#     "fields": ["*"],
#     "_source": False
# }))

# pp(search_document(es, index_name, {
#     "fields": ["user.first"],
#     "_source": False
# }))

# pp(search_document(es, index_name, {
#     "_source": False,
#     "query": {
#         "match": {
#             "user.id": "kimchy"
#         }
#     }
# }))

# pp(search_document(es, index_name, {
#     "_source": "http.*",
#     "query": {
#         "match": {
#             "user.id": "kimchy"
#         }
#     }
# }))

# pp(search_document(es, index_name, {
#     "_source": ["geo.*", 'source.*'],
#     "query": {
#         "match": {
#             "user.id": "kimchy"
#         }
#     }
# }))

# pp(search_document(es, index_name, {
#     "_source": {
#         "includes": ["geo.*", "source.*", 'http.*'],
#         "excludes": ["http.response"]
#     },
#     "query": {
#         "term": {
#             "user.id": "kimchy"
#         }
#     }
# }))


# Search templates
# pp(es.put_script(id='search-news-template', body={
#   "script": {
#     "lang": "mustache",
#     "source": {
#       'query': {
#             'multi_match': {
#                 'query': '{{q}}',
#                 'fields': ['title', 'content'],
#             }
#         },
#       '_source': ['title', 'content'],
#       "from": "{{from}}",
#       "size": "{{size}}"
#     },
#     "params": {
#         "q": "hello world",
#         "from": 0,
#         "size": 10
#     }
#   }
# }))

# pp(es.render_search_template(body={
#     "id": "search-news-template",
#     "params": {
#         "q": "水电站",
#         "from": 20,
#         "size": 10
#     }
# }))

# pp(es.search_template(index='news', body={
#     "id": "search-news-template",
#     "params": {
#         "q": "水电站",
#         "from": 0,
#         "size": 10
#     }
# }))

# pp(es.put_script(id='search-characters-template', body={
#   "script": {
#     "lang": "mustache",
#     "source": {
#       'query': {
#             'term': {'name': '{{q}}'}
#         },
#       '_source': ['name', 'image', 'url'],
#       "from": "{{from}}{{^from}}0{{/from}}",
#       "size": "{{size}}{{^size}}10{{/size}}"
#     }
#   }
# }))

# pp(es.render_search_template(body={
#     "id": "search-characters-template",
#     "params": {
#         "q": "何立峰",
#     }
# }))

# pp(es.get_script(id='search-news-template'))
# pp(es.get_script(id='search-characters-template'))
# pp(es.delete_script(id='search-characters-template'))

# pp(es.search_template(index='characters', body={
#     "id": "search-characters-template",
#     "params": {
#         "q": "何立峰",
#         "from": 0,
#         "size": 10
#     }
# }))


# Sort search results
# pp(search_document(es, 'news', {
#     'query': {
#         'multi_match': {
#             'query': '外商投资',
#             'fields': ['title', 'content'],
#         }
#     },
#     '_source': ['title', 'publish_time'],
#     "sort": [
#         {"publish_time": {"order": "desc"}},
#         # {"title": "desc"},
#         "_score"
#     ],
#     # "track_scores": True,
# }))


pp(get_mapping(es, 'news'))
