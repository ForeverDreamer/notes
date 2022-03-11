from datetime import datetime as dt
import json
from pprint import pprint as pp

from elasticsearch import Elasticsearch
es = Elasticsearch()

# print(es.cat.indices(v=True))
# res = None


# 2 Modeling Data in Elasticsearch


# 6) Demo: Default Mappings
# res = es.indices.create(index='books')
# res = es.indices.get_mapping(index=['books'])

# body = {
#     'name': 'Harry Potter',
#     'author': 'J.K.Rowling',
#     'cost': '325.00',
#     'Available': 'true',
#     'publishers': 'Bloomsbury',
#     'date': '1997-06-27'
# }
#
# res = es.index(index='books', id=1, body=body)
# res = es.indices.get_mapping(index=['books'])

# 只能新增字段，不能修改已有字段
# body = {
#     'properties': {
#         # 'pages': {
#         #     'type': 'integer'
#         # },
#         # elasticsearch.exceptions.RequestError: RequestError(400, 'illegal_argument_exception',
#         # 'mapper [cost] cannot be changed from type [text] to [integer]')
#         'cost': {
#             'type': 'integer'
#         }
#     }
# }
#
# res = es.indices.put_mapping(body=body, index=['books'])
# res = es.indices.get_mapping(index=['books'])

# res = es.indices.delete(index=['books'])

# 7) Demo: Numeric and Date Detection
# res = es.index(index='my_index', body={'count': '5'})
# res = es.indices.get_mapping(index=['my_index'])

# body = {
#     'mappings': {
#         'numeric_detection': True
#     }
# }
#
# res = es.indices.create(index='my_index1', body=body)
# res = es.indices.get_mapping(index=['my_index1'])

# 自动识别为'long'类型
# res = es.index(index='my_index1', body={'count': '5'})
# res = es.indices.get_mapping(index=['my_index1'])

# 识别为‘string’类型
# res = es.index(index='my_index2', body={'create_date': '20/09/2017'})
# res = es.indices.get_mapping(index=['my_index2'])

# 自动识别为'date'类型
# res = es.index(index='my_index3', body={'create_date': '2017/09/02'})
# res = es.indices.get_mapping(index=['my_index3'])

# body = {
#     'mappings': {
#         'date_detection': False
#     }
# }
#
# res = es.indices.create(index='my_index4', body=body)
# 识别为‘string’类型
# res = es.index(index='my_index4', body={'create_date': '2017/09/02'})
# res = es.indices.get_mapping(index=['my_index4'])

# 8) Demo: Explicit Mappings

# body = {
#     'settings': {
#         'number_of_shards': 1,
#         'number_of_replicas': 0
#     },
#     # 'dynamic': 'strict',  # 'true'/'false'/'strict', 7.9.3不支持
#     'mappings': {
#         'properties': {
#             'title': {'type': 'text'},
#             'author': {'type': 'text'},
#             'available': {'type': 'boolean'},
#             'pages': {'type': 'integer'},
#             'cost': {'type': 'float'},
#             'published': {
#                 'type': 'date',
#                 'format': 'YYYY-MM-DD'
#             }
#         }
#     }
# }

# res = es.indices.create(index='books', body=body)
# res = es.indices.get_mapping(index=['books'])
# res = es.indices.get_settings(index=['books'])

# body = {
#     'mappings': {
#         '_source': {'enabled': False},
#         # '_all': {'enabled': False},  # 7.9.3不支持
#         'properties': {
#             'title': {'type': 'text'},
#             'director': {'type': 'text'},
#             'actors': {'type': 'object'},
#             'released': {
#                 'type': 'date',
#                 'format': 'YYYY-MM-DD'
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='movies', body=body)
# res = es.indices.get_mapping(index=['movies'])

# 9) Demo: Mapped vs. Unmapped Fields

# res = es.index(index='products', body={'name': 'Multi grain bread', 'cost': '55', 'discount': '20'})
# res = es.indices.get_mapping(index=['products'])

# res = es.search(body={'query': {'wildcard': {'discount': '2*'}}}, index='products')

# body = {
#     'mappings': {
#         'properties': {
#             'name': {'type': 'text'},
#             'cost': {'type': 'integer'},
#             'discount': {'type': 'integer'}
#         }
#     }
# }
#
# res = es.indices.create(index='products_copy', body=body)

# res = es.index(index='products_copy', body={'name': 'Multi grain bread', 'cost': '55', 'discount': '20'})
# res = es.indices.get_mapping(index=['products_copy'])

# elasticsearch.exceptions.RequestError: RequestError(400, 'search_phase_execution_exception',
# 'Can only use wildcard queries on keyword, text and wildcard fields - not on [discount] which is of type [integer]')
# res = es.search(body={'query': {'wildcard': {'discount': '2*'}}}, index='products_copy')

# res = es.search(body={'query': {'match': {'discount': '20'}}}, index='products_copy')
# res = es.search(body={'query': {'match': {'discount': 20}}}, index='products_copy')

# res = es.index(index='blog', body={'name': 'Top 10 Ocean Mysteries', 'date': '18-06-2017'})
# res = es.indices.get_mapping(index=['blog'])

# res = es.search(body={'query': {'match': {'date': '18-06-2017'}}}, index='blog')
# res = es.search(body={'query': {'term': {'date': '18-06'}}}, index='blog')
# res = es.search(body={'query': {'term': {'date': '18-06-2017'}}}, index='blog')

# body = {
#     'mappings': {
#         'properties': {
#             'name': {'type': 'text'},
#             'date': {
#                 'type': 'date',
#                 'format': 'DD-MM-YYYY'
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='blog_copy', body=body)
# res = es.indices.get_mapping(index=['blog_copy'])

# res = es.index(index='blog_copy', body={'name': 'Top 10 Ocean Mysteries', 'date': '18-06-2017'})

# elasticsearch.exceptions.RequestError: RequestError(400, 'search_phase_execution_exception', 'failed to parse date
# field [18-06] with format [DD-MM-YYYY]: [failed to parse date field [18-06] with format [DD-MM-YYYY]]')
# res = es.search(body={'query': {'match': {'date': '18-06'}}}, index='blog_copy')

# res = es.search(body={'query': {'match': {'date': '18-06-2017'}}}, index='blog_copy')
# res = es.search(body={'query': {'term': {'date': '18-06-2017'}}}, index='blog_copy')

# 10) Demo: Dynamic Templates for Custom Mapping

# body = {
#     'mappings': {
#         'dynamic_templates': [
#             {
#                 'integers': {
#                     'match_mapping_type': 'long',
#                     'mapping': {
#                         'type': 'integer'
#                     }
#                 }
#             },
#             {
#                 'strings': {
#                     'match_mapping_type': 'string',
#                     'mapping': {
#                         'type': 'text'
#                     }
#                 }
#             }
#         ]
#     }
# }
#
# res = es.indices.create(index='index_one', body=body)
# res = es.indices.get_mapping(index=['index_one'])

# res = es.index(index='index_one', body={'an_integer': 3200000, 'a_string': 'Random string'})
# res = es.indices.get_mapping(index=['index_one'])

# body = {
#     'mappings': {
#         'dynamic_templates': [
#             {
#                 'longs_as_strings': {
#                     'match_mapping_type': 'string',
#                     'match': 'long_*',
#                     'unmatch': '*_text',
#                     'mapping': {
#                         'type': 'long'
#                     }
#                 }
#             }
#         ]
#     }
# }
#
# res = es.indices.create(index='index_two', body=body)
#
# res = es.index(index='index_two', body={'long_num': '32', 'long_text': 'boom'})
# res = es.indices.get_mapping(index=['index_two'])

# body = {
#     'mappings': {
#         'dynamic_templates': [
#             {
#                 'full_name': {
#                     'path_match': 'name.*',
#                     'path_unmatch': '*.middle',
#                     'mapping': {
#                         'type': 'text',
#                         'copy_to': 'full_name',
#                     }
#                 }
#             }
#         ]
#     }
# }
#
# res = es.indices.create(index='index_three', body=body)
#
# res = es.index(index='index_three', body={'name': {'first': 'Harry', 'middle': 'James', 'last': 'Potter'}})
# res = es.indices.get_mapping(index=['index_three'])

# body = {
#     "query": {"match_all": {}},
# }
# body = {
#     'query': {
#         'match': {
#             # 'full_name': {
#             #     'query': 'Harry Potter'
#             # }
#             # 'name.first': {
#             #     'query': 'Harry'
#             # }
#             'name.last': {
#                 'query': 'Potter'
#             }
#         }
#     }
# }
# res = es.search(index='question_answer_1', body=body)

# 11) Demo: Character Filters and Token Filters

# body = {
#     'tokenizer': 'keyword',
#     'char_filter': ['html_strip'],
#     'text': '<p>I&apos;m so <b>sad</b>!</p>'
# }
#
# res = es.indices.analyze(body=body)

# body = {
#     'settings': {
#         'analysis': {
#             'analyzer': {
#                 'my_analyzer': {
#                     'tokenizer': 'keyword',
#                     'char_filter': [
#                         'my_char_filter'
#                     ]
#                 }
#             },
#             'char_filter': {
#                 'my_char_filter': {
#                     'type': 'mapping',
#                     'mappings': [
#                         '零 => 0',
#                         '一 => 1',
#                         '二 => 2',
#                         '三 => 3',
#                         '四 => 4',
#                         '五 => 5',
#                         '六 => 6',
#                         '七 => 7',
#                         '八 => 8',
#                         '九 => 9',
#                     ]
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='sample_index', body=body)

# body = {
#     'analyzer': 'my_analyzer',
#     'text': 'My license plate is 六三二五八零'
# }
#
# res = es.indices.analyze(index='sample_index', body=body)
# res = es.indices.analyze(index='books', body={'text': 'My license plate is 六三二五八零'})

# body = {
#     'settings': {
#         'analysis': {
#             'analyzer': {
#                 'my_analyzer': {
#                     'tokenizer': 'standard',
#                     'char_filter': [
#                         'my_char_filter'
#                     ]
#                 }
#             },
#             'char_filter': {
#                 'my_char_filter': {
#                     'type': 'pattern_replace',
#                     'pattern': '(\\d+)-(?=\\d)',
#                     'replacement': '$1_',
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='sample_index_two', body=body)

# body = {
#     'analyzer': 'my_analyzer',
#     'text': 'My credit card is 123-456-789'
# }
#
# res = es.indices.analyze(index='sample_index_two', body=body)

# body = {
#     'settings': {
#         'analysis': {
#             'analyzer': {
#                 'standard_lowercase_example': {
#                     'type': 'custom',
#                     'tokenizer': 'standard',
#                     'filter': ['lowercase']
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='lowercase_example', body=body)

# body = {
#     'text': 'The QUICK Brown Fox'
# }
#
# res = es.indices.analyze(index='lowercase_example', body=body)

# 12) Demo: Built-in and Custom Analyzers

# body = {
#     'analyzer': 'standard',
#     'text': 'The 5 boxing wizards jump quickly.'
# }
#
# res = es.indices.analyze(body=body)

# body = {
#     'analyzer': 'simple',
#     'text': 'The 5 boxing wizards jump quickly.'
# }
#
# res = es.indices.analyze(body=body)

# body = {
#     'analyzer': 'whitespace',
#     'text': 'The 5 boxing wizards jump quickly.'
# }
#
# res = es.indices.analyze(body=body)

# body = {
#     'analyzer': 'stop',
#     'text': 'The 5 boxing wizards jump quickly.'
# }
#
# res = es.indices.analyze(body=body)

# body = {
#     'mappings': {
#         'properties': {
#             'text': {
#                 'type': 'text',
#                 'fields': {
#                     'english': {
#                         'type': 'text',
#                         'analyzer': 'english'
#                     }
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='index_four', body=body)

# body = {
#     'field': 'text',
#     'text': 'Begin at the beginning.'
# }
#
# res = es.indices.analyze(index='index_four', body=body)

# body = {
#     'field': 'text.english',
#     'text': 'Begin at the beginning.'
# }
#
# res = es.indices.analyze(index='index_four', body=body)

# body = {
#     'settings': {
#         'analysis': {
#             'analyzer': {
#                 'my_custom_analyzer': {
#                     'type': 'custom',
#                     'char_filter': [
#                         'emoticons'
#                     ],
#                     'tokenizer': 'punctuation',
#                     'filter': [
#                         'lowercase',
#                         'english_stop'
#                     ]
#                 }
#             },
#             'tokenizer': {
#                 'punctuation': {
#                     'type': 'pattern',
#                     'pattern': '[.,!?]'
#                 }
#             },
#             'char_filter': {
#                 'emoticons': {
#                     'type': 'mapping',
#                     'mappings': [
#                         ':) => _happy_',
#                         ':( => _sad_'
#                     ]
#                 }
#             },
#             'filter': {
#                 'english_stop': {
#                     'type': 'stop',
#                     'stopwords': '_english_'
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='index_five', body=body)

# body = {
#     'analyzer': 'my_custom_analyzer',
#     'text': 'I am a :) person, and you?'
# }
#
# res = es.indices.analyze(index='index_five', body=body)


# 3 Managing Relational Content

# 4) Demo: Denormalizing Data

# body = {
#     'title': 'Fanfictions',
#     'date': '2016-07-18',
#     'user': {
#         'id': '1',
#         'name': 'James'
#     }
# }
#
# res = es.index(index='index_posts', body=body)

# res = es.search(body={'query': {'match': {'user.name': 'James'}}}, index='index_posts')
# res = es.indices.get_mapping(index=['index_posts'])

# 5) Demo: Nested Objects

# body = {
#     'name': 'John Green',
#     'books': [
#         {
#             'name': 'The Fault in Our Stars',
#             'genre': 'Romance',
#             'publisher': 'Penguin'
#         },
#         {
#             'name': 'Turtles All the Way Down',
#             'genre': 'YA',
#             'publisher': 'Dutton'
#         }
#     ]
# }
#
# res = es.index(index='authors', body=body)
#
# body = {
#     'name': 'Jay Asher',
#     'books': [
#         {
#             'name': 'Thirteen Reasons Why',
#             'genre': 'YA',
#             'publisher': 'Penguin'
#         }
#     ]
# }
#
# res = es.index(index='authors', body=body)
# res = es.indices.get_mapping(index=['authors'])

# body = {
#     "query": {
#         'bool': {
#             'must': [
#                 {'match': {'books.genre': 'YA'}},
#                 {'match': {'books.publisher': 'Penguin'}}
#             ]
#         }
#     }
# }
#
# res = es.search(index='authors', body=body)

# res = es.indices.delete(index=['authors'])

# body = {
#     'mappings': {
#         'properties': {
#             'books': {
#                 'type': 'nested'
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='authors', body=body)
# res = es.indices.get_mapping(index=['authors'])

# body = {
#     'name': 'John Green',
#     'books': [
#         {
#             'name': 'The Fault in Our Stars',
#             'genre': 'Romance',
#             'publisher': 'Penguin'
#         },
#         {
#             'name': 'Turtles All the Way Down',
#             'genre': 'YA',
#             'publisher': 'Dutton'
#         }
#     ]
# }
#
# res = es.index(index='authors', body=body)
#
# body = {
#     'name': 'Jay Asher',
#     'books': [
#         {
#             'name': 'Thirteen Reasons Why',
#             'genre': 'YA',
#             'publisher': 'Penguin'
#         }
#     ]
# }
#
# res = es.index(index='authors', body=body)

# body = {
#     "query": {
#         'bool': {
#             'must': [
#                 {'match': {'name': 'John Green'}},
#                 {
#                     'nested': {
#                         'path': 'books',
#                         'query': {
#                             'bool': {
#                                 'must': [
#                                     {'match': {'books.genre': 'YA'}},
#                                     {'match': {'books.publisher': 'Penguin'}}
#                                 ]
#                             }
#                         }
#                     }
#                 }
#             ]
#         }
#     }
# }
#
# res = es.search(index='authors', body=body)

# body = {
#     "query": {
#         'bool': {
#             'must': [
#                 {'match': {'name': 'John Green'}},
#                 {
#                     'nested': {
#                         'path': 'books',
#                         'query': {
#                             'bool': {
#                                 'must': [
#                                     {'match': {'books.genre': 'YA'}},
#                                     {'match': {'books.publisher': 'Dutton'}}
#                                 ]
#                             }
#                         }
#                     }
#                 }
#             ]
#         }
#     }
# }
#
# res = es.search(index='authors', body=body)

# 8) Demo: Parent Child Documents Using Join

# body = {
#     'mappings': {
#         'properties': {
#             'my_join_field': {
#                 'type': 'join',
#                 'relations': {'question': 'answer'}
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='question_answer', body=body)
# res = es.indices.get_mapping(index=['question_answer'])

# body = {
#     'text': 'This is question one',
#     'my_join_field': {'name': 'question'}
# }
#
# res = es.index(index='question_answer', body=body, id=1)
#
# body = {
#     'text': 'This is question two',
#     'my_join_field': {'name': 'question'}
# }
#
# res = es.index(index='question_answer', body=body, id=2)
#
# body = {
#     'text': 'This is the first answer',
#     'my_join_field': {'name': 'answer', 'parent': '1'}
# }
#
# res = es.index(index='question_answer', body=body, id=3, params={'routing': 1})
#
# body = {
#     'text': 'This is another answer to the first question',
#     'my_join_field': {'name': 'answer', 'parent': '1'}
# }
#
# res = es.index(index='question_answer', body=body, id=4, params={'routing': 1})
#
# body = {
#     'text': 'This is second answer',
#     'my_join_field': {'name': 'answer', 'parent': '2'}
# }
#
# res = es.index(index='question_answer', body=body, id=5, params={'routing': 2})

# 9) Demo: Querying Child Documents Using Parent ID

# body = {
#     'query': {"parent_id": {'type': 'answer', 'id': 1}},
# }

# body = {
#     'query': {"parent_id": {'type': 'answer', 'id': 2}},
# }

# body = {
#     'query': {"parent_id": {'type': 'answer', 'id': 1}},
#     'aggs': {
#         'parents': {
#             'terms': {
#                 'field': 'my_join_field#question',
#                 'size': 10
#             }
#         }
#     }
# }

# 10) Demo: Has Child, Has Parent Queries

# body = {
#     'query': {
#         'has_child': {
#             'type': 'answer',
#             'query': {
#                 'match_all': {}
#             }
#         }
#     }
# }

# body = {
#     'query': {
#         'has_parent': {
#             'parent_type': 'question',
#             'query': {
#                 'match_all': {}
#             }
#         }
#     }
# }

# 11) Demo: Children Aggregation

# body = {
#     'my_join_field': {
#         'name': 'question'
#     },
#     'body': '<p>Cookies too flat, they spread and thin out while baking...<p>',
#     'title': 'How do I get my cookies shaped right?',
#     'tags': ['cookie-baking', 'baking']
# }
# res = es.index(index='question_answer', body=body, id=6)

# body = {
#     'my_join_field': {
#         'name': 'answer',
#         'parent': '6'
#     },
#     'owner': {
#         'location': 'Norfolk, united Kingdom',
#         'display_name': 'Sam',
#         'id': 48
#     },
#     'body': '<p>Usually that happens when the dough is not properly chilled...<p>',
#     'creation_date': '2009-05-04T13:45:37.030'
# }
# res = es.index(index='question_answer', body=body, id=7, params={'routing': 6})

# body = {
#     'my_join_field': {
#         'name': 'answer',
#         'parent': '6'
#     },
#     'owner': {
#         'location': 'Norfolk, united Kingdom',
#         'display_name': 'Judy',
#         'id': 49
#     },
#     'body': '<p>Use butter if the dough is too soft before baking...<p>',
#     'creation_date': '2009-05-05T13:45:37.030'
# }
# res = es.index(index='question_answer', body=body, id=8, params={'routing': 6})

# body = {
#     'aggs': {
#         'top-tags': {
#             'terms': {
#                 'field': 'tags.keyword',
#                 'size': 10
#             }
#         }
#     }
# }

# body = {
#     'aggs': {
#         'top-tags': {
#             'terms': {
#                 'field': 'tags.keyword',
#                 'size': 10
#             },
#             'aggs': {
#                 'to-answers': {
#                     'children': {
#                         'type': 'answer'
#                     },
#                     'aggs': {
#                         'top-names': {
#                             'terms': {
#                                 'field': 'owner.display_name.keyword',
#                                 'size': 10
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }
#
# res = es.search(index='question_answer', body=body)

# 11) Demo: Multi-level Joins

# body = {
#     'mappings': {
#         'properties': {
#             'my_join_field': {
#                 'type': 'join',
#                 'relations': {
#                     'question': ['answer', 'comment'],
#                     'answer': 'vote'
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.create(index='question_answer_1', body=body)
# res = es.indices.get_mapping(index=['question_answer_1'])

# body = {
#     'text': 'This is question one',
#     'my_join_field': {'name': 'question'}
# }
#
# res = es.index(index='question_answer_1', body=body, id=1)

# body = {
#     'text': 'This is the first answer',
#     'my_join_field': {'name': 'answer', 'parent': '1'}
# }
#
# res = es.index(index='question_answer_1', body=body, id=2, params={'routing': 1})

# body = {
#     'text': 'This is a comment',
#     'my_join_field': {'name': 'comment', 'parent': '1'}
# }
#
# res = es.index(index='question_answer_1', body=body, id=3, params={'routing': 1})

# body = {
#     'text': 'This is a vote',
#     'my_join_field': {'name': 'vote', 'parent': '2'}
# }
#
# res = es.index(index='question_answer_1', body=body, id=4, params={'routing': 2})

# body = {
#     "query": {"match_all": {}},
# }

# body = {
#     'query': {"parent_id": {'type': 'vote', 'id': 2}},
# }

# res = es.search(index='question_answer_1', body=body)


# 5 Designing for Scale

# 4) Demo: Index Templates
# body = {
#     'index_patterns': 'logstash-*',
#     'priority': 0,
#     'template': {
#         'settings': {
#                 'number_of_shards': 1
#         },
#         'mappings': {
#             '_source': {
#                 'enabled': False
#             },
#             'properties': {
#                 'host_name': {
#                     'type': 'keyword'
#                 },
#                 'created_at': {
#                     'type': 'text'
#                 }
#             }
#         }
#     }
# }
#
# res = es.indices.put_index_template(name='logstash-', body=body)

# res = es.indices.get_index_template()
# res = es.indices.get_index_template(name='logstash-')
# res = es.indices.exists_index_template(name='logstash-')
# res = es.indices.delete_index_template(name='logstash-')

# body = {
#     'host_name': '64.242.88.10',
#     'created_at': str(dt.now()),
#     'request': 'GET /mailman/listinfo/hsdivision HTTP/1.1'
# }
#
# res = es.index(index='logstash-202112', id=1, body=body)
# res = es.indices.get_mapping(index=['logstash-202112'])

# body = {
#     'index_patterns': 'logsta*',
#     'priority': 1,
#     'template': {
#         'settings': {
#                 'number_of_shards': 2
#         },
#         'mappings': {
#             '_source': {
#                 'enabled': False
#             },
#             'properties': {
#                 'host_name': {
#                     'type': 'text'
#                 },
#                 'created_at': {
#                     'type': 'text'
#                 }
#             }
#         }
#     }
# }
# res = es.indices.put_index_template(name='logsta', body=body)
#
# body = {
#     'host_name': '64.242.88.10',
#     'created_at': str(dt.now()),
#     'request': 'GET /twiki/bin/view/TWiki/SvenDowideit HTTP/1.1'
# }
#
# res = es.index(index='logstash-202202', id=1, body=body)
res = es.indices.get_mapping(index=['logstash-202202'])

# res = es.indices.get_index_template(name='logs*')
# res = es.indices.delete_index_template(name='logs')

# 6) Demo: Using Index Aliases
# res = es.cat.aliases()
#
pp(res)
