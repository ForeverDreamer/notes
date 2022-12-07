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
share_util = ShareUtil(engine)
share_util.eval(BASE_DIR + 'utils/jsx/init.jsx')

# time.sleep(CALL_INTERVAL)
# share_util.open_project('D:/Untitled Project.aep')
# share_util.set_anchor_point(3, ['Transform', 'Anchor Point'], 'TOP_LEFT', 'false')
with open(BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf.json', "r") as f:
    conf = json.loads(f.read())
share_util.import_files(conf['files'])

time.sleep(CALL_INTERVAL)
precomp_util = PrecompUtil(engine)
precomp_util.create_many(conf['precomps'])

time.sleep(CALL_INTERVAL)
share_util.create_subtitles(conf['subtitles'])

time.sleep(CALL_INTERVAL)
share_util.create_annotations(conf['annotations'])

time.sleep(CALL_INTERVAL)
camera_util = CameraUtil(engine)
camera_util.add_many(conf['cameras'])
