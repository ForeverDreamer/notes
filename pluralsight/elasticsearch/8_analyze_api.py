from pprint import pprint as pp

from elasticsearch import Elasticsearch

from es_utils import *

# es = Elasticsearch()
es = Elasticsearch('http://192.168.71.20:9200')

# 人物和组织名称需要作为专有词处理
# ik_max_word: 何, 立, 峰, 穆, 虹, 离, 退, 局, 外商投资, 外商, 投资, 办公厅, 办公, 厅
# ik_smart: 何, 立, 峰, 穆, 虹, 离, 退, 局, 外商投资, 办公厅
# query = ' 何立峰 穆虹 离退局 外商投资 办公厅'

# ik_max_word: 林, 念, 修, 连, 维, 良, 离, 退, 局, 外债, 规模, 驻, 委, 纪检监察, 纪检, 监察, 组
# ik_smart: 林, 念, 修, 连, 维, 良, 离, 退, 局, 外债, 规模, 驻, 委, 纪检监察, 组
# query = ' 林念修 连维良 离退局 外债规模 驻委纪检监察组'
#
# # analyzer = 'ik_max_word'
# analyzer = 'ik_smart'
#
# body = {
#     'analyzer': analyzer,
#     'text': query
# }
# res = es.indices.analyze(body=body)
# print(', '.join([t['token'] for t in res['tokens']]))


pp_tokens(analyze(es, 'services', {
    "text": "外债规模",
    "analyzer": "pinyin_analyzer"
}))

# pp_tokens(analyze(es, 'news', {
#     # "text": ["周杰伦", "李连杰", "成龙"],
#     "text": "周杰伦 李连杰 成龙",
#     "analyzer": "pinyin_analyzer"
# }))

# pp(get_settings(es, 'characters'))
# pp(get_mapping(es, 'characters'))
# pp(get_mapping(es, 'organizations'))
# pp(get_mapping(es, 'services'))
pp(get_mapping(es, 'news'))
