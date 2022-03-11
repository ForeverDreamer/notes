from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()


# Query and filter context
pp(search_document(es, 'news', {
    "query": {
        "bool": {
            "must": [
                {"match": {"title": "何立峰"}},
                {"match": {"content": "何立峰"}}
            ],
            "filter": [
                {"range": {"publish_time": {"gte": "2020-01-01 00:00:00"}}}
            ]
        }
    },
    '_source': ['title', 'publish_time'],
}))

# Term-level queries
# Term
# pp(search_document(es, 'news', {
#     'query': {
#         'term': {
#             'title': '外商投资',
#         }
#     },
#     '_source': ['title', 'publish_time'],
# }))

# Terms
# pp(search_document(es, 'news', {
#     'query': {
#         'terms': {
#             'title': ['水电站', '外商'],
#         }
#     },
#     '_source': ['title', 'publish_time'],
# }))

# Wildcard
# pp(search_document(es, 'news', {
#     'query': {
#         'wildcard': {
#             'title': '*投资',
#         }
#     },
#     '_source': ['title', 'publish_time'],
# }))