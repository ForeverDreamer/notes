from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()

# pp(delete_index(es, 'medcl'))

pp(create_index(es, 'medcl', {
    "settings": {
        "analysis": {
            "analyzer": {
                "pinyin_analyzer": {
                    "tokenizer": "my_pinyin"
                }
            },
            "tokenizer": {
                "my_pinyin": {
                    "type": "pinyin",
                    "keep_separate_first_letter": False,
                    "keep_full_pinyin": True,
                    "keep_original": True,
                    "limit_first_letter_length": 16,
                    "lowercase": True,
                    "remove_duplicated_term": True
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "name": {
                "type": "keyword",
                "fields": {
                    "pinyin": {
                        "type": "text",
                        "store": False,
                        "term_vector": "with_offsets",
                        "analyzer": "pinyin_analyzer",
                        "boost": 10
                    }
                }
            }
        }
    }
}))

pp_tokens(analyze(es, 'medcl', {
    "text": ["刘德华"],
    "analyzer": "pinyin_analyzer"
}))

# pp(add_document(es, 'medcl', 'andy', {"name": "刘德华"}))

# pp(get_mapping(es, 'medcl'))

# pp(search_document(es, 'medcl', {
#     "query": {
#         "match": {
#             "name": "刘德华"
#         }
#     },
# }))

# pp(search_document(es, 'medcl', {
#     "query": {
#         "match": {
#             "name.pinyin": "刘德"
#         }
#     },
# }))

# pp(search_document(es, 'medcl', {
#     "query": {
#         "match": {
#             "name.pinyin": "liu"
#         }
#     },
# }))

# pp(search_document(es, 'medcl', {
#     "query": {
#         "match": {
#             "name.pinyin": "ldh"
#         }
#     },
# }))

pp(search_document(es, 'medcl', {
    "query": {
        "match": {
            "name.pinyin": "de+hua"
        }
    },
}))