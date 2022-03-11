from pprint import pprint as pp

from elasticsearch import Elasticsearch, helpers

from elasticsearch_learning.es_utils import *

es = Elasticsearch()

# pp(delete_index(es, '_all'))


# 3 Executing Low-level Index Control

# 4) Demo: Configuring Similarity Models
# pp(create_index(es, 'similarity_model_1', {
#     'settings': {
#         'index': {
#             'similarity': {
#                 'default': {
#                     'type': 'BM25'
#                 }
#             }
#         }
#     }
# }))
# pp(get_settings(es, 'similarity_model_1'))
# pp(add_document(es, index='similarity_model_1', doc_id='1', body={'id': '01', 'name': 'John Smith'}))
# pp(search_document(es, 'similarity_model_1', {'query': {'match': {'name': 'John Smith'}}}))

# pp(close_index(es, 'similarity_model_1'))
# pp(put_settings(
#     es,
#     {'index': {'similarity': {'default': {'type': 'boolean'}}}},
#     'similarity_model_1',
# ))
# pp(get_settings(es, 'similarity_model_1'))
# pp(open_index(es, 'similarity_model_1'))
# pp(search_document(es, 'similarity_model_1', {'query': {'match': {'name': 'John Smith'}}}))

# 5) Demo: Configuring Per-field Similarity Models
# pp(create_index(es, 'similarity_model_2', {
#     'mappings': {
#         'properties': {
#             'id_default_sim': {
#                 'type': 'text'
#             },
#             'status_boolean_sim': {
#                 'type': 'text',
#                 'similarity': 'boolean'
#             }
#         }
#     }
# }))
# pp(add_document(es, index='similarity_model_2', doc_id='1', body={
#     'id_default_sim': '01',
#     'name': 'John Smith',
#     'status_boolean_sim': True
# }))
# pp(get_mapping(es, 'similarity_model_2'))
# pp(search_document(es, 'similarity_model_2', {'query': {'term': {'id_default_sim': '01'}}}))
# pp(search_document(es, 'similarity_model_2', {'query': {'match': {'name': 'John Smith'}}}))
# pp(search_document(es, 'similarity_model_2', {'query': {'term': {'status_boolean_sim': True}}}))

# 6) Demo: Custom Similarity Models
# pp(create_index(es, 'similarity_model_3', {
#     'settings': {
#         'index': {
#             'similarity': {
#                 'my_similarity': {
#                     'type': 'LMDirichlet',
#                     'mu': 2000,
#                 }
#             }
#         }
#     }
# }))
# pp(put_mapping(
#     es,
#     {'properties': {'title': {'type': 'text', 'similarity': 'my_similarity'}}},
#     'similarity_model_3'
# ))
# pp(get_mapping(es, 'similarity_model_3'))
# pp(add_document(es, 'similarity_model_3', '1', {'title': 'The British Queen'}))
# pp(search_document(es, 'similarity_model_3', {'query': {'match': {'title': 'British Queen'}}}))
# pp(search_document(es, 'similarity_model_3', {'query': {'match': {'title': 'British Monarch'}}}))

# 8) Demo: Force Merge Segments
# pp(create_index(es, 'merge_segments_1', {
#     'settings': {
#         'number_of_shards': 2,
#         'number_of_replicas': 0,
#         'index.merge.policy.expunge_deletes_allowed': 1,
#     }
# }))
#
#
# def gen_create_data():
#     for i in range(100):
#         yield {
#             '_op_type': 'create',
#             '_index': 'merge_segments_1',
#             '_id': i+4,
#             '_source': {'name': f'doc-{i+4}'}
#         }
#
#
# pp(helpers.bulk(es, gen_create_data()))

# pp(es.indices.segments(index='merge_segments_1'))
# print(es.cat.segments(index='merge_segments_1', params={'v': 'true'}))


# def gen_delete_data():
#     for i in range(4):
#         yield {
#             '_op_type': 'delete',
#             '_index': 'merge_segments_1',
#             '_id': i+1,
#         }
#
#
# pp(helpers.bulk(es, gen_delete_data()))
# pp(es.indices.segments(index='merge_segments_1'))
# print(es.cat.segments(index='merge_segments_1', params={'v': 'true'}))
# pp(es.indices.forcemerge(
#     index='merge_segments_1',
#     params={'max_num_segments': 1, 'flush': 'false', 'only_expunge_deletes': 'false'}
# ))
# print(es.nodes.hot_threads())
# pp(es.indices.segments(index='merge_segments_1'))
# print(es.cat.segments(index='merge_segments_1', params={'v': 'true'}))

# 10) Demo: Shard Request Caching
# pp(add_document(es, 'caching_1', '1', {'id': '01', 'name': 'John Smith'}))
# pp(search_document(es, 'caching_1', {'query': {'match': {'name': 'John Smith'}}}))
# pp(es.nodes.stats())

# 4 Improving the User Search Experience

# 5) Demo: Term and Match Queries
# pp(add_document(es, 'term_match_queries', '1', {'id': '01', 'name': 'Jane Smith', 'status': 'true'}))
# pp(add_document(es, 'term_match_queries', '2', {'id': '02', 'name': 'James Smith', 'status': 'false'}))
# pp(get_mapping(es, index=['term_match_queries']))

# 搜不到
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'jane smith'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'Jane Smith'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'Jane'}}}))
# 搜得到
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'jane'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'match': {'name': 'Jane'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'match': {'name': 'Jane Smith'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'match': {'name': 'james smith'}}}))

# pp(delete_index(es, 'term_match_queries'))
# pp(create_index(es, 'term_match_queries', {'mappings': {'properties': {'name': {'type': 'keyword'}}}}))
# pp(add_document(es, 'term_match_queries', '1', {'id': '01', 'name': 'Jane Smith', 'status': 'true'}))
# pp(add_document(es, 'term_match_queries', '2', {'id': '02', 'name': 'James Smith', 'status': 'false'}))
# pp(get_mapping(es, 'term_match_queries'))
# 搜不到
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'Jane'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'match': {'name': 'jane smith'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'jane smith'}}}))
# 搜得到
# pp(search_document(es, 'term_match_queries', {'query': {'term': {'name': 'Jane Smith'}}}))
# pp(search_document(es, 'term_match_queries', {'query': {'match': {'name': 'Jane Smith'}}}))
# pp(delete_index(es, 'term_match_queries'))

# 6) Demo: Case Insensitive Term Searches with Normalizers
# elasticsearch.exceptions.RequestError: RequestError(400, 'mapper_parsing_exception', 'unknown parameter [analyzer]
# on mapper [name] of type [keyword]')
# keyword类型不支持analyzer
# pp(create_index(es, 'index_one', {
#     'settings': {
#         'analysis': {
#             'analyzer': {
#                 'sample_analyzer': {
#                     'type': 'custom',
#                     'tokenizer': 'keyword',
#                     'filter': [
#                         'lowercase',
#                     ]
#                 }
#             }
#         }
#     },
#     'mappings': {
#         'properties': {
#             'name': {
#                 'type': 'keyword',
#                 'analyzer': 'sample_analyzer',
#             }
#         }
#     }
# }))

# pp(create_index(es, 'index_one', {
#     'settings': {
#         'analysis': {
#             'normalizer': {
#                 'my_normalizer': {
#                     'type': 'custom',
#                     'char_filter': [],
#                     'filter': 'lowercase'
#                 }
#             }
#         }
#     },
#     'mappings': {
#         'properties': {
#             'name': {
#                 'type': 'keyword',
#                 'normalizer': 'my_normalizer',
#             }
#         }
#     }
# }))

# pp(add_document(es, 'index_one', '1', {'id': '01', 'name': 'Jane Smith', 'status': 'true'}))
# pp(add_document(es, 'index_one', '2', {'id': '02', 'name': 'James Smith', 'status': 'false'}))
# 搜得到
# pp(search_document(es, 'index_one', {'query': {'term': {'name': 'jane smith'}}}))
# pp(delete_index(es, 'index_one'))

# 7) Demo: Suggesters
# pp(add_document(es, 'books', '1', {'id': '01', 'title': 'Harry Potter and The Chamber of Secrets', 'author': 'J K Rowling'}))
# pp(add_document(es, 'books', '2', {'id': '02', 'title': 'Harry Potter and The Prisoner of Azkaban', 'author': 'J K Rowling'}))
# pp(add_document(es, 'books', '3', {'id': '03', 'title': 'Papertowns', 'author': 'John Green'}))
# pp(add_document(es, 'books', '4', {'id': '04', 'title': 'Paperhouse', 'author': 'Jean Janzen'}))
# pp(add_document(es, 'books', '5', {'id': '05', 'title': 'Black Beauty', 'author': 'Anna Sewell'}))
# pp(add_document(es, 'books', '6', {'id': '06', 'title': 'Black Boy', 'author': 'Richard Wright'}))

# 可用于智能纠错
# pp(search_document(es, 'books', {'suggest': {'my-suggestion': {'text': 'paperhouns', 'term': {'field': 'title'}}}}))
# pp(search_document(es, 'books', {'suggest': {'my-suggestion': {'text': 'pattertowns', 'term': {'field': 'title'}}}}))
# pp(search_document(es, 'books', {
#     'query': {
#         'match': {
#             'title': 'blank beauty'
#         }
#     },
#     'suggest': {
#         'my-suggestion': {
#             'text': 'blank beauty',
#             'term': {
#                 'field': 'title'
#             }
#         }
#     }
# }))
# pp(delete_index(es, 'books'))

# pp(create_index(es, 'books', {
#     'settings': {
#         'index': {
#             'number_of_shards': 1,
#             'analysis': {
#                 'analyzer': {
#                     'trigram': {
#                         'type': 'custom',
#                         'tokenizer': 'standard',
#                         # elasticsearch.exceptions.RequestError: RequestError(400, 'illegal_argument_exception',
#                         # 'The [standard] token filter has been removed.')
#                         # 'filter': ['standard', 'shingle']
#                         'filter': ['shingle']
#                     }
#                 }
#             }
#         }
#
#     },
#     'mappings': {
#         'properties': {
#             'title': {
#                 'type': 'text',
#                 'fields': {
#                     'trigram': {
#                         'type': 'text',
#                         'analyzer': 'trigram'
#                     }
#                 },
#             }
#         }
#     }
# }))

# pp(add_document(es, 'books', None, {'title': 'noble warriors'}))
# pp(add_document(es, 'books', None, {'title': 'nobel prize'}))

# pp(search_document(es, 'books', {'query': {'match_all': {}}}))

# pp(search_document(es, 'books', {
#     'suggest': {
#         'text': 'noble prize',
#         'simple_phrase': {
#             'phrase': {
#                 'field': 'title.trigram',
#                 'size': 1,
#                 'gram_size': 3,
#                 'direct_generator': [
#                     {
#                         'field': 'title.trigram',
#                         'suggest_mode': 'always'
#                     }
#                 ]
#             }
#         }
#     }
# }))

# pp(create_index(es, 'music', {
#     'mappings': {
#         'properties': {
#             'suggest': {
#                 'type': 'completion'
#             },
#             'title': {
#                 'type': 'keyword'
#             }
#         }
#     }
# }))

# pp(add_document(es, 'music', '1', {
#     'suggest': ['Everything has changed', 'Everybody knows', 'Every night in my dreams']
# }))
# pp(search_document(es, index='music', body={'query': {'match_all': {}}}))
# pp(get_mapping(es, 'music'))

# pp(search_document(es, 'music', {
#     'suggest': {
#         'song_suggest': {
#             'prefix': 'ever',
#             'completion': {
#                 'field': 'suggest'
#             }
#         }
#     }
# }))

# pp(create_index(es, 'place', {
#     'mappings': {
#         'properties': {
#             'suggest': {
#                 'type': 'completion',
#                 'contexts': [
#                     {
#                         'name': 'place_type',
#                         'type': 'category'
#                     },
#                     {
#                         'name': 'location',
#                         'type': 'geo',
#                         'precision': 4
#                     }
#                 ]
#             }
#         }
#     }
# }))

# pp(add_document(es, 'place', '1', {
#     'suggest': {
#         'input': ['mcdonalds', 'big bear', 'chicking'],
#         'contexts': {
#             'place_type': ['cafe', 'food']
#         }
#     }
# }))
# pp(add_document(es, 'place', '2', {
#     'suggest': {
#         'input': ['drunken monkey', 'big pitcher'],
#         'contexts': {
#             'place_type': ['pub', 'food']
#         }
#     }
# }))

# pp(search_document(es, 'place', {
#     '_source': False,
#     'suggest': {
#         'place_suggestion': {
#             'prefix': 'big',
#             'completion': {
#                 'field': 'suggest',
#                 'size': 10,
#                 'contexts': {
#                     'place_type': ['cafe', 'pub']
#                 }
#             }
#         }
#     }
# }))

# pp(search_document(es, 'place', {
#     '_source': False,
#     'suggest': {
#         'place_suggestion': {
#             'prefix': 'big',
#             'completion': {
#                 'field': 'suggest',
#                 'size': 10,
#                 'contexts': {
#                     'place_type': [
#                         {'context': 'cafe'},
#                         {'context': 'pub', 'boost': 2}
#                     ]
#                 }
#             }
#         }
#     }
# }))

# 8) Demo: Fuzzy Search
# pp(create_index(es, 'members', {
#     'mappings': {
#         'properties': {
#             'idno': {
#                 'type': 'keyword'
#             }
#         }
#     }
# }))

# pp(add_document(es, 'members', '1', {'idno': 'ABC01'}))
# pp(add_document(es, 'members', '2', {'idno': 'XYZ01'}))

# 搜得到
# pp(search_document(es, 'members', {'query': {'fuzzy': {'idno': 'BC01'}}}))
# pp(search_document(es, 'members', {'query': {'fuzzy': {'idno': 'XYZ0'}}}))
# pp(search_document(es, 'members', {'query': {'fuzzy': {'idno': 'AB01'}}}))
# 搜不到
# pp(search_document(es, 'members', {'query': {'fuzzy': {'idno': 'AB10'}}}))
# pp(search_document(es, 'members', {'query': {'fuzzy': {'idno': 'XYZ'}}}))
# 搜得到
# pp(search_document(es, 'members', {
#     'query': {
#         'fuzzy': {
#             'idno': {
#                 'value': 'AB10',
#                 'boost': 1.0,
#                 'fuzziness': 2,
#                 'prefix_length': 0,
#                 'max_expansions': 100
#             }
#         }
#     }
# }))
# pp(search_document(es, 'members', {
#     'query': {
#         'fuzzy': {
#             'idno': {
#                 'value': 'XYZ',
#                 'boost': 1.0,
#                 'fuzziness': 2,
#                 'prefix_length': 0,
#                 'max_expansions': 100
#             }
#         }
#     }
# }))

# 9) Demo: Autocomplete
# pp(delete_index(es, 'blog'))
# pp(create_index(es, 'blog', {
#     'settings': {
#         'analysis': {
#             'filter': {
#                 'autocomplete_filter': {
#                     'type': 'edge_ngram',
#                     'min_gram': 1,
#                     'max_gram': 20
#                 }
#             },
#             'analyzer': {
#                 'autocomplete': {
#                     'type': 'custom',
#                     'tokenizer': 'standard',
#                     'filter': ['lowercase', 'autocomplete_filter']
#                 }
#             }
#         }
#     },
#     'mappings': {
#         'properties': {
#             'title': {
#                 'type': 'text',
#                 'analyzer': 'autocomplete',
#                 'search_analyzer': 'standard'
#             }
#         }
#     }
# }))

# pp(add_document(es, 'blog', '1', {'title': 'Pilates vs Yoga', 'author': 'Jane Smith'}))
# pp(add_document(es, 'blog', '2', {'title': 'PCOS and Fitness', 'author': 'Jane Smith'}))

# pp(search_document(es, 'blog', {
#     'query': {
#         'match': {
#             'title': {
#                 'query': 'Pilate vs Yo',
#                 'operator': 'and'
#             }
#         }
#     }
# }))
# pp(search_document(es, 'blog', {
#     'query': {
#         'match': {
#             'title': {
#                 'query': 'PCO',
#                 'operator': 'and'
#             }
#         }
#     }
# }))


# 5 Dealing with Human Languages

# 2) Demo: Creating an Index Per Language
# pp(create_index(es, 'blogs-english', {
#     'mappings': {
#         'properties': {
#             'title': {
#                 'type': 'text',
#                 'analyzer': 'english'
#             }
#         }
#     }
# }))
# pp(add_document(es, 'blogs-english', '1', {'id': '01', 'title': 'The Meaning of Dreams'}))
# pp(add_document(es, 'blogs-english', '2', {'id': '02', 'title': 'The Deja Vu'}))
#
# pp(create_index(es, 'blogs-french', {
#     'mappings': {
#         'properties': {
#             'title': {
#                 'type': 'text',
#                 'analyzer': 'french'
#             }
#         }
#     }
# }))
# pp(add_document(es, 'blogs-french', '1', {'id': '01', 'title': 'le cortex frontal'}))
# pp(add_document(es, 'blogs-french', '2', {'id': '02', 'title': 'Le Deja Vu'}))

# pp(search_document(es, 'blogs-*', {'query': {'match': {'title': 'deja vu'}}}))
# pp(search_document(es, 'blogs-*', {
#     'query': {
#         'match': {'title': 'deja vu'}
#     },
#     'indices_boost': {
#         'blogs-french': 3,
#         'blogs-english': 2
#     }
# }))

# 3) Demo: Setting a Per-field Language Analyzer
# pp(create_index(es, 'blogs-movies', {
#     'mappings': {
#         'properties': {
#             'title': {
#                 'type': 'text'
#             },
#             'title_nw': {
#                 'type': 'text',
#                 'analyzer': 'norwegian'
#             },
#             'title_pg': {
#                 'type': 'text',
#                 'analyzer': 'portuguese'
#             },
#             'title_fr': {
#                 'type': 'text',
#                 'analyzer': 'french'
#             },
#             'title_es': {
#                 'type': 'text',
#                 'analyzer': 'spanish'
#             }
#         }
#     }
# }))
# pp(add_document(es, 'blogs-movies', '1', {
#     'id': '01',
#     'title': 'The Shawshank Redemption',
#     'title_nw': 'Frihetensregn',
#     'title_pg': 'Um sonho de liberdade',
#     'title_fr': '法语字符串（没有输入法）',
#     'title_es': 'Cadena perpetua'
# }))
# 搜不到
# pp(search_document(es, 'blogs-movies', {'query': {'term': {'title': 'Frihetensregn'}}}))
# 搜得到
# pp(search_document(es, 'blogs-movies', {'query': {'multi_match': {'query': 'Frihetensregn', 'fields': 'title*'}}}))
# boost 'title_nw'
# pp(search_document(es, 'blogs-movies', {'query': {'multi_match': {'query': 'Frihetensregn', 'fields': ['title*', 'title_nw^2']}}}))

# 4) Demo: Multiple Languages in the Same Field
# pp(delete_index(es, 'movies'))
# pp(create_index(es, 'movies', {
#     'mappings': {
#         'properties': {
#             'title': {
#                 'type': 'text',
#                 'fields': {
#                     'de': {
#                         'type': 'text',
#                         'analyzer': 'german'
#                     },
#                     'en': {
#                         'type': 'text',
#                         'analyzer': 'english'
#                     },
#                     'fr': {
#                         'type': 'text',
#                         'analyzer': 'french'
#                     },
#                     'es': {
#                         'type': 'text',
#                         'analyzer': 'spanish'
#                     }
#                 }
#             }
#         }
#     }
# }))
# pp(add_document(es, 'movies', '1', {'id': '01', 'title': 'Guardians of The Galaxy'}))
# pp(add_document(es, 'movies', '2', {'id': '02', 'title': 'Cest la vie'}))
# pp(add_document(es, 'movies', '3', {'id': '03', 'title': '西班牙语（没有输入法）'}))
# pp(search_document(es, 'movies', {'query': {'match': {'title': 'Cest la vie'}}}))
# pp(search_document(es, 'movies', {'query': {'match': {'title': 'Invisible Guardian'}}}))

# 5) Demo: The ICU Plugin
# Dockerfile安装步骤
# 1.修改Dockerfile
# FROM elasticsearch:6.8.3
# RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
# 2.build镜像
# docker build -t elasticsearch .

# 运行容器安装步骤
# 1.docker exec -it ruidu_es /bin/bash
# 2./usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
# 3.重启docker

# 删除插件
# /usr/share/elasticsearch/bin/elasticsearch-plugin remove analysis-icu

# 本地安装ik
# 1.下载https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.14.2/elasticsearch-analysis-ik-7.14.2.zip
# 2.docker cp 'C:\Users\micro\Downloads\elasticsearch-analysis-ik-7.14.2.zip' ruidu_es:/usr/share/elasticsearch/plugins
# 3.cd /usr/share/elasticsearch/plugins
#   mkdir ik
#   mv elasticsearch-analysis-ik-7.14.2.zip ./ik
#   unzip elasticsearch-analysis-ik-7.14.2.zip
#   rm -rf elasticsearch-analysis-ik-7.14.2.zip
# 4.重启docker

# pp(create_index(es, 'icu_sample', {
#     'settings': {
#         'index': {
#             'analysis': {
#                 'analyzer': {
#                     'my_icu_analyzer': {
#                         'tokenizer': 'icu_tokenizer'
#                     }
#                 }
#             }
#         }
#     }
# }))
# pp(analyze(es, 'icu_sample', {
#     'analyzer': 'my_icu_analyzer',
#     'text': '中华人民共和国万岁'
# }))

# 先创建一个配置文件/usr/share/elasticsearch/config/keywordTokenizer.rbbi
# http://unicode.org/iso15924/iso15924-codes.html
pp(create_index(es, 'icu_custom_sample', {
    'settings': {
        'index': {
            'analysis': {
                'tokenizer': {
                  'icu_user_file': {
                      'type': 'icu_tokenizer',
                      'rule_fiels': 'Arab:keywordTokenizer.rbbi'
                  }
                },
                'analyzer': {
                    'my_analyzer': {
                        'type': 'custom',
                        'tokenizer': 'icu_user_file'
                    }
                }
            }
        }
    }
}))
