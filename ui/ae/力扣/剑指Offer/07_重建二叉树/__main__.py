import json
import time

from ae.constants.share import BASE_DIR, CALL_INTERVAL
from ae.utils.py.camera import CameraUtil
from ae.utils.py.engine import Engine
from ae.utils.py.precomp import PrecompUtil
from ae.utils.py.share import ensure_app_started, ShareUtil

# Ae窗口最小化时找不到标题，导致程序阻塞，坑！
# ensure_app_started()

engine = Engine(version="18.0")
# engine.start_app()
statements = []
share_util = ShareUtil(engine)
# statements += share_util.eval(BASE_DIR + 'utils/jsx/init.jsx')
statements += share_util.head('力扣/剑指Offer/07_重建二叉树/conf.json')
statements += share_util.body()
# time.sleep(CALL_INTERVAL)
# share_util.open_project('D:/Untitled Project.aep')
# share_util.set_anchor_point(3, ['Transform', 'Anchor Point'], 'TOP_LEFT', 'false')
# with open(BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf.json', "r") as f:
#     conf = json.loads(f.read())
# 代码执行的顺序决定了Layers的顺序，合理安排代码执行顺序，避免创建好之后需要再调整Layer顺序
# statements += share_util.import_files(conf['files'])
# statements += share_util.create_scenes(conf['scenes'])

# time.sleep(CALL_INTERVAL)
# precomp_util = PrecompUtil(engine)
# statements += precomp_util.create_many(conf['precomps'])
#
# time.sleep(CALL_INTERVAL)
# statements += share_util.create_subtitles(conf['subtitles'])
#
# time.sleep(CALL_INTERVAL)
# statements += share_util.create_annotations(conf['annotations'])
#
# time.sleep(CALL_INTERVAL)
# camera_util = CameraUtil(engine)
# statements += camera_util.add_many(conf['cameras'])
statements += share_util.tail()
engine.execute('__main__', statements)
