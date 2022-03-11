from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()


# 新建ruiso.dic并参照其它*.dic文件添加专业词汇,
# 修改专业词汇配置文件plugins/ik/config/IKAnalyzer.cfg.xml, <entry key="ext_dict">ruiso.dic</entry>
# 重启elasticsearch
# pp_tokens(analyze(es, 'news', {
#     'analyzer': 'ik_smart',
#     'text': '周杰伦永远的神'
# }))
#
# pp_tokens(analyze(es, 'news', {
#     'analyzer': 'ik_smart',
#     'text': '坚持一带一路政策'
# }))
#
# pp_tokens(analyze(es, 'news', {
#     'analyzer': 'ik_smart',
#     'text': '今天天气绝绝子'
# }))

pp_tokens(analyze(es, 'news', {
    'analyzer': 'ik_max_word',
    'text': '大众创业万众创新'
}))

pp_tokens(analyze(es, 'news', {
    'analyzer': 'ik_smart',
    'text': '大众创业万众创新'
}))
