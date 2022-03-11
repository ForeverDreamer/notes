from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()


# Test an analyzer
# pp(analyze(es, {
#     "analyzer": "whitespace",
#     "text": "The quick brown fox."
# }))

# pp(analyze(es, {
#     "tokenizer": "standard",
#     "filter": ["lowercase", "asciifolding"],
#     "text": "Is this déja vu?"
# }))

# pp(delete_index(es, 'my-index-000001'))

# pp(create_index(es, 'my-index-000001', {
#     "settings": {
#         "analysis": {
#             "analyzer": {
#                 "std_folded": {
#                     "type": "custom",
#                     "tokenizer": "standard",
#                     "filter": [
#                         "lowercase",
#                         "asciifolding"
#                     ]
#                 }
#             }
#         }
#     },
#     "mappings": {
#         "properties": {
#             "my_text": {
#                 "type": "text",
#                 "analyzer": "std_folded"
#             }
#         }
#     }
# }))

# pp(analyze(es, 'my-index-000001', {
#         "analyzer": "std_folded",
#         "text": "Is this déjà vu?"
# }))

# pp(analyze(es, 'my-index-000001', {
#   "field": "my_text",
#   "text":  "Is this déjà vu?"
# }))


# Configuring built-in analyzers
# pp(delete_index(es, 'my-index-000001'))

# pp(create_index(es, 'my-index-000001', {
#     "settings": {
#         "analysis": {
#             "analyzer": {
#                 "std_english": {
#                     "type": "standard",
#                     "stopwords": "_english_"
#                 }
#             }
#         }
#     },
#     "mappings": {
#         "properties": {
#             "my_text": {
#                 "type": "text",
#                 "analyzer": "standard",
#                 "fields": {
#                     "english": {
#                         "type": "text",
#                         "analyzer": "std_english"
#                     }
#                 }
#             }
#         }
#     }
# }))

# pp(analyze(es, 'my-index-000001', {
#     "field": "my_text",
#     "text": "The old brown cow"
# }))

# pp(analyze(es, 'my-index-000001', {
#     "field": "my_text.english",
#     "text": "The old brown cow"
# }))


# Create a custom analyzer
# pp(delete_index(es, 'my-index-000001'))

# pp(create_index(es, 'my-index-000001', {
#     "settings": {
#         "analysis": {
#             "analyzer": {
#                 "my_custom_analyzer": {
#                     "type": "custom",
#                     "tokenizer": "standard",
#                     "char_filter": [
#                         "html_strip"
#                     ],
#                     "filter": [
#                         "lowercase",
#                         "asciifolding"
#                     ]
#                 }
#             }
#         }
#     }
# }))

# pp(analyze(es, 'my-index-000001', {
#     "analyzer": "my_custom_analyzer",
#     "text": "Is this <b>déjà vu</b>?"
# }))

# pp(delete_index(es, 'my-index-000001'))

# pp(create_index(es, 'my-index-000001', {
#     "settings": {
#         "analysis": {
#             "analyzer": {
#                 "my_custom_analyzer": {
#                     "char_filter": [
#                         "emoticons"
#                     ],
#                     "tokenizer": "punctuation",
#                     "filter": [
#                         "lowercase",
#                         "english_stop"
#                     ]
#                 }
#             },
#             "tokenizer": {
#                 "punctuation": {
#                     "type": "pattern",
#                     "pattern": "[ .,!?]"
#                 }
#             },
#             "char_filter": {
#                 "emoticons": {
#                     "type": "mapping",
#                     "mappings": [
#                         ":) => _happy_",
#                         ":( => _sad_"
#                     ]
#                 }
#             },
#             "filter": {
#                 "english_stop": {
#                     "type": "stop",
#                     "stopwords": "_english_"
#                 }
#             }
#         }
#     }
# }))

# pp(analyze(es, 'my-index-000001', {
#     "analyzer": "my_custom_analyzer",
#     "text": "I'm a :) person, and you?"
# }))


# Specify an analyzer
# pp(delete_index(es, 'my-index-000001'))

# Specify the analyzer for a field
# pp(create_index(es, 'my-index-000001', {
#     "mappings": {
#         "properties": {
#             "title": {
#                 "type": "text",
#                 "analyzer": "whitespace"
#             }
#         }
#     }
# }))

# Specify the default analyzer for an index
# pp(create_index(es, 'my-index-000001', {
#     "settings": {
#         "analysis": {
#             "analyzer": {
#                 "default": {
#                     "type": "simple"
#                 }
#             }
#         }
#     }
# }))

# Specify the search analyzer for a query
# pp(search_document(es, 'my-index-000001', {
#     "query": {
#         "match": {
#             "message": {
#                 "query": "Quick foxes",
#                 "analyzer": "stop"
#             }
#         }
#     }
# }))

# Specify the search analyzer for a field
# pp(create_index(es, 'my-index-000001', {
#     "mappings": {
#         "properties": {
#             "title": {
#                 "type": "text",
#                 "analyzer": "whitespace",
#                 "search_analyzer": "simple"
#             }
#         }
#     }
# }))

# Specify the default search analyzer for an index
pp(create_index(es, 'my-index-000001', {
    "settings": {
        "analysis": {
            "analyzer": {
                "default": {
                    "type": "simple"
                },
                "default_search": {
                    "type": "whitespace"
                }
            }
        }
    }
}))
