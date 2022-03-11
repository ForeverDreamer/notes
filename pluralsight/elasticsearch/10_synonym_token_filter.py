from pprint import pprint as pp

from elasticsearch import Elasticsearch

from elasticsearch_learning.es_utils import *

es = Elasticsearch()

# https://segmentfault.com/a/1190000022886681
# https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-synonym-tokenfilter.html
# config/analysis/synonyms.txt，按官方文档格式说明配置同义词
index_name = 'synonym_filter'
# pp(delete_index(es, index_name))
# pp(create_index(es, index_name, {
#   "settings": {
#     "analysis": {
#       "filter": {
#         "synonym_filter": {
#           "type": "synonym",
#           "expand": True,
#           "synonyms_path": "analysis/synonyms.txt"
#         }
#       },
#       "analyzer": {
#         "synonym_analyzer": {
#           "tokenizer": "ik_max_word",
#           "filter": [
#             "synonym_filter"
#           ]
#         },
#         "synonym_search_analyzer": {
#           "tokenizer": "ik_smart",
#           "filter": [
#             "synonym_filter"
#           ]
#         }
#       }
#     }
#   },
#   "mappings": {
#     "properties": {
#       "title": {
#         "type": "text",
#         "analyzer": "synonym_analyzer",
#         "search_analyzer": "synonym_search_analyzer"
#       }
#     }
#   }
# }))

posts = [
  ('国务院办公厅关于进一步支持大学生创新创业的指导意见', '生是大众创业万众创新的生力军,支持大学生创新创业具有重要意义。近年来,越来越多的大学生投身创新创业实践,但也面临融资难、经验少、服务不到位等问题。'),
  ('国务院关于开展营商环境<em>创新</em>试点工作的意见', '探索在民用建筑工程领域推进和完善建筑师负责制。 (七)更好支持市场主体<em>创新</em>发展。完善<em>创新</em>资源配置方式和管理机制,探索适应新业态新模式发展需要的准入准营标准,提升市场主体<em>创新</em>力。'),
  ('国务院办公厅关于建设第三批<em>大众创业万众创新</em>示范基地的通知', '>三、加强组织领导 各有关部门要加强对<em>双创</em>示范基地的协调指导和日常管理,充分发挥推进<em>大众创业万众创新</em>部际联席会议制度统筹作用,加大对<em>双创</em>示范基地建设的支持力度。'),
  ('国务院办公厅关于提升<em>大众创业万众创新</em>示范基地带动作用进一步促改革稳就业强动能的实施意见', '国务院办公厅关于 提升<em>大众创业万众创新</em>示范基地带动作用 进一步促改革稳就业强动能的实施意见 国办发〔2020〕26号 各省、自治区、直辖市人民政府,国务院各部委、各直属机构: <em>大众创业万众创新</em>示范基地启动...'),
  ('国务院关于推动<em>创新</em><em>创业</em>高质量发展打造“<em>双创</em>”升级版的意见', '随着<em>大众创业万众创新</em>蓬勃发展,<em>创新</em><em>创业</em>环境持续改善,<em>创新</em><em>创业</em>主体日益多元,各类支撑平台不断丰富,<em>创新</em><em>创业</em>社会氛围更加浓厚,<em>创新</em><em>创业</em>理念日益深入人心,取得显著成效。'),
  ('关于延续执行<em>创业</em>投资企业和天使投资个人投资初创科技型企业有关政策条件的公告', '关于延续执行<em>创业</em>投资企业和天使投资个人投资初创科技型企业有关政策条件的公告 财政部 税务总局公告2022年第6号 为进一步支持<em>创业</em><em>创新</em>,现就<em>创业</em>投资企业和天使投资个人投资初创科技型企业所得税政策有关事项公...'),
  ('工业和信息化部关于<em>大众</em>消费领域北斗推广应用的若干意见', '举办北斗<em>大众</em>消费领域应用征集大赛和<em>创新</em>论坛,形成北斗<em>创新</em>应用案例集,推广一批北斗新应用,拓宽北斗应用服务新航道。 四、健全完善产业生态 (七)扶持企业做优做强。'),
  ('国家发展改革委等部门关于深入实施<em>创业</em>带动就业示范行动 力促高校毕业生<em>创业</em>就业的通知', '大众创业万众创新</em>示范基地(以下简称示范基地)组织实施<em>创业</em>带动就业示范行动(以下简称示范行动),在推动<em>创业</em>带动就业方面积累了有益经验、取得了积极成效。'),
  ('十部门关于加快推进竹产业<em>创新</em>发展的意见', '引导竹产业高新技术企业发展壮大,积极培育科技型中小企业,打造<em>创新</em>型企业集群。引导企业在核心技术攻关、科技人才培养、科技成果转化等方面加大投入力度。鼓励科技人员到企业<em>创新</em><em>创业'),
  ('科技部关于支持新一批城市开展<em>创新</em>型城市建设的通知', '有关城市要围绕实施<em>创新</em>驱动发展战略,加快推进建设方案重点任务落实,持续深化体制机制改革,优化<em>创新</em><em>创业</em>生态,打造人才高地,扩大开放合作,增强自主<em>创新</em>能力,提供高质量科技供给,促进科技成果转化,培育壮大新产...'),
  ('服务<em>创新</em>发展 完善管理机制——第二轮“双一流”建设有关情况解读', '新华社北京2月14日电 题:服务<em>创新</em>发展 完善管理机制——第二轮“双一流”建设有关情况解读 新华社记者 王鹏 记者14日从教育部获悉,教育部、财政部、国家发展改革委日前印发《关于深入推进世界一流大学和一流...'),
  ('《“十四五”旅游业发展规划》发布——<em>大众</em>旅游新阶段 旅游业如何向上生长', '和互动性。 《规划》将“坚持<em>创新</em>驱动发展”放在七项重点任务之首,提出要充分运用数字化、网络化、智能化科技<em>创新</em>成果,升级传统旅游业态,<em>创新</em>产品和服务方式,推动旅游业从资源驱动向<em>创新</em>驱动转变。'),
  ('“十四五”行业发展规划指明方向——以<em>创新</em>驱动重塑旅游业', '北京交通大学旅游管理系教授张辉说,我国旅游业要实现高质量发展,在注重技术<em>创新</em>以外,尤其要关注制度<em>创新</em>,从需求侧入手,通过制度<em>创新</em>释放消费需求,同时要研究管理<em>创新</em>,更好发挥协会、商会等组织的作用。'),
  ('掌握就业<em>创业</em>真本领,端上勤劳<em>创新</em>致富“金饭碗”——《“十四五”职业技能培训规划》解读', '新华社北京1月7日电 题:掌握就业<em>创业</em>真本领,端上勤劳<em>创新</em>致富“金饭碗”——《“十四五”职业技能培训规划》解读 新华社记者 叶昊鸣 近日,《“十四五”职业技能培训规划》正式印发,对未来我国职业技能培训工作...'),
  ('三方面举措纵深推进<em>大众创业万众创新', '新华社北京6月23日电(记者 赵文君)“坚持<em>创业</em>带动就业”“营造更优<em>双创</em>发展生态”“强化<em>创业</em><em>创新</em>政策激励”,22日召开的国务院常务会议部署“十四五”时期纵深推进<em>大众创业万众创新</em>的三方面举措,更大激发市场活...'),
  ('国务院关于开展营商环境<em>创新</em>试点工作的意见', '探索在民用建筑工程领域推进和完善建筑师负责制。 (七)更好支持市场主体<em>创新</em>发展。完善<em>创新</em>资源配置方式和管理机制,探索适应新业态新模式发展需要的准入准营标准,提升市场主体<em>创新'),
  ('国务院办公厅关于印发“十四五”文物保护和科技<em>创新</em>规划的通知<br> “十四五”文物保护和科技<em>创新</em>规划', '四、全面加强文物科技<em>创新</em> 坚持科技<em>创新</em>引领,遵循文物保护和考古特点规律,加大要素投入力度,优化资源配置,加强多学科协同,构建产学研用深度融合的文物科技<em>创新</em>体系,推进行业标准体系建设,提升文物科技<em>创新</em>能力...'),
  ('国务院办公厅关于进一步支持大学生<em>创新</em><em>创业</em>的指导意见', '发展战略的重要支撑,大学生是<em>大众创业万众创新</em>的生力军,支持大学生<em>创新</em><em>创业</em>具有重要意义。近年来,越来越多的大学生投身<em>创新</em><em>创业</em>实践,但也面临融资难、经验少、服务不到位等问题。'),
  ('国务院关于同意在全面深化服务贸易<em>创新</em>发展试点地区暂时调整实施有关行政法规和国务院<br> 文件规定的批复', '现批复如下: 一、按照《国务院关于同意全面深化服务贸易<em>创新</em>发展试点的批复》(国函〔2020〕111号)要求,同意自即日起至2023年8月1日,在全面深化服务贸易<em>创新</em>发展试点地区暂时调整实施《旅行社条例》、...'),
  ('国务院印发关于推进自由贸易试验区贸易投资便利化改革<em>创新</em>若干措施的通知<br> 关于推进自由贸易试验区贸易投资便利化改革创新的若干举措', '(交通运输部负责) 三、开展进口贸易<em>创新</em> 支持自贸试验区所在地培育进口贸易促进<em>创新</em>示范区,综合利用提高便利化水平、<em>创新</em>贸易模式、提升公共服务等多种手段,推动进口领域监管制度、商业模式、配套服务等多方面<em>创新'),
]

for title, content in posts:
  es.index(index=index_name, id=None, body={
    'title': title,
    'content': content,
  })

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '我爱吃西红柿'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '我爱吃番茄'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '我爱吃圣女果'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '我爱吃洋芋'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '我爱吃马铃薯'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '我爱吃土豆'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_analyzer',
#     'text': '习大大出国访问'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_search_analyzer',
#     'text': '习主席出国访问'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_search_analyzer',
#     'text': '习近平出国访问'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_search_analyzer',
#     'text': '访问2233'
# }))

# pp(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_search_analyzer',
#     'text': '上B站'
# }))

# pp_tokens(analyze(es, 'synonym_filter', {
#     'analyzer': 'synonym_search_analyzer',
#     'text': '看二次元'
# }))

pp_tokens(analyze(es, 'synonym_filter', {
    'analyzer': 'synonym_search_analyzer',
    'text': '双创'
}))
