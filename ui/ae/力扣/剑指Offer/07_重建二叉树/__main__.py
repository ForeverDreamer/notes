from ae.utils.engine import Engine
from ae.utils.share import ensure_app_started, ShareUtil

ensure_app_started()

engine = Engine(version="18.0", base_dir='D:\\data_files\\notes\\ui\\ae\\力扣\\剑指Offer\\07_重建二叉树\\')
share_util = ShareUtil(engine)
# share_util.open_project('D:/Untitled Project.aep')
share_util.set_anchor_point(3, ['Transform', 'Anchor Point'], 'TOP_LEFT', 'false')
