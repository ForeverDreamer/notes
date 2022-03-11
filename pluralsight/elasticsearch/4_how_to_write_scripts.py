from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()

# pp(add_document(es, 'my-index-000001', '1', {'my_field': 5}))


# Use parameters in your script & Shorten your script
# pp(search_document(es, 'my-index-000001', {
#   "script_fields": {
#     "my_doubled_field": {
#       "script": {
#         "source": "doc['my_field'].value * params['multiplier']",
#         "params": {
#           "multiplier": 2
#         }
#       }
#     }
#   }
# }))


# Store and retrieve scripts
# pp(es.put_script(id='calculate-score', body={
#   "script": {
#     "lang": "painless",
#     "source": "Math.log(_score * 2) + params['my_modifier']"
#   }
# }))

# pp(es.get_script(id='calculate-score'))
# pp(search_document(es, 'my-index-000001', {
#   "query": {
#     "term": {
#             "my_field": 5
#         }
#   }
# }))

# pp(search_document(es, 'my-index-000001', {
#   "query": {
#     "script_score": {
#       "query": {
#         "term": {
#             "my_field": 5
#         }
#       },
#       "script": {
#         "id": "calculate-score",
#         "params": {
#           "my_modifier": 2
#         }
#       }
#     }
#   }
# }))

# pp(es.delete_script(id='calculate-score'))


# Update documents with scripts
# pp(replace_document(es, 'my-index-000001', '1', {
#     "counter": 1,
#     "tags": ["red"]
# }))

# pp(update_document(es, 'my-index-000001', '1', {
#     "script": {
#         "source": "ctx._source.counter += params.count",
#         "lang": "painless",
#         "params": {
#             "count": 4
#         }
#     }
# }))

# pp(search_document(es, 'my-index-000001', {
#     'query': {'match_all': {}}
# }))

# pp(update_document(es, 'my-index-000001', '1', {
#     "script": {
#         "source": "ctx._source.tags.add(params['tag'])",
#         "lang": "painless",
#         "params": {
#             "tag": "blue"
#         }
#     }
# }))

# pp(search_document(es, 'my-index-000001', {
#     'query': {'match_all': {}}
# }))

# pp(update_document(es, 'my-index-000001', '1', {
#     "script": {
#         "source": "if (ctx._source.tags.contains(params['tag'])) { ctx._source.tags.remove(ctx._source.tags.indexOf(params['tag'])) }",
#         "lang": "painless",
#         "params": {
#             "tag": "blue"
#         }
#     }
# }))

# pp(search_document(es, 'my-index-000001', {
#     'query': {'match_all': {}}
# }))

# pp(update_document(es, 'my-index-000001', '1', {
#     "script": "ctx._source.new_field = 'value_of_new_field'"
# }))

# pp(search_document(es, 'my-index-000001', {
#     'query': {'match_all': {}}
# }))

# pp(update_document(es, 'my-index-000001', '1', {
#     "script": "ctx._source.remove('new_field')"
# }))

# pp(search_document(es, 'my-index-000001', {
#     'query': {'match_all': {}}
# }))

# pp(update_document(es, 'my-index-000001', '1', {
#     "script": {
#         "source": "if (ctx._source.tags.contains(params['tag'])) { ctx.op = 'delete' } else { ctx.op = 'none' }",
#         "lang": "painless",
#         "params": {
#             "tag": "red"
#         }
#     }
# }))

pp(search_document(es, 'my-index-000001', {
    'query': {'match_all': {}}
}))
