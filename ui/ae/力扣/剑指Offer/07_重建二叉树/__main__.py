import json
import time

from ae.constants.share import BASE_DIR, CALL_INTERVAL
from ae.utils.py.camera import Camera
from ae.utils.py.engine import Engine
from ae.utils.py.precomp import Precomp
from ae.utils.py.share import ensure_app_started, Share

ensure_app_started()

engine = Engine(version="18.0", base_dir=BASE_DIR)
# engine.start_app()
share = Share(engine)
share.eval(BASE_DIR + 'utils/jsx/init.jsx')

time.sleep(CALL_INTERVAL)
# share_util.open_project('D:/Untitled Project.aep')
# share_util.set_anchor_point(3, ['Transform', 'Anchor Point'], 'TOP_LEFT', 'false')
with open(BASE_DIR + '力扣/剑指Offer/07_重建二叉树/conf.json', "r") as f:
    conf = json.loads(f.read())
share.import_files(conf['files'])

time.sleep(CALL_INTERVAL)
share.create_precomps(conf['precomps'])

time.sleep(CALL_INTERVAL)
camera = Camera(engine)
camera.add_many(conf['cameras'])
