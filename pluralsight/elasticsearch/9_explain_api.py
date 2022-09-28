import os
from pprint import pprint as pp

from elasticsearch import Elasticsearch

from es_utils import *

es = Elasticsearch()

# pp(get_settings(es, 'news'))
# pp(get_mapping(es, 'news'))


def score_details(hits, index, body):
    for hit in hits:
        # pp(hit)
        print('-----------------------------------------------------')
        print('_id: ', hit['_id'])
        res = explain(es, index, hit['_id'], body)
        space = ' '
        print((res['explanation']['value'], res['explanation']['description']))
        for d1 in res['explanation']['details']:
            print(space * 2, d1['value'], d1['description'])
            for d2 in d1['details']:
                print(space * 4, d2['value'], d2['description'])


news_body = {
    'query': {
        'multi_match': {
            'query': '何立峰 穆虹 离退局 外商投资 办公厅',
            'fields': ['title', 'content'],
        }
    },
}
news = search_document(es, 'news', news_body)
score_details(news['hits']['hits'], 'news', news_body)


# services_body = {
#     'query': {
#         'match': {'stem': '外商投资'}
#     }
# }
# services = search_document(es, 'services', services_body)
# score_details(services['hits']['hits'], 'services', services_body)


# organizations_body = {
#     'query': {
#         'term': {'name': '办公厅'}
#     }
# }
# organization = search_document(es, 'organizations', organizations_body)
# score_details(organization['hits']['hits'], 'organizations', organizations_body)


# characters_body = {
#     'query': {
#         'term': {'name': '何立峰'}
#     }
# }
# character = search_document(es, 'characters', characters_body)
# score_details(character['hits']['hits'], 'characters', characters_body)
