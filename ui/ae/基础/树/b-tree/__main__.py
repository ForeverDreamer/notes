from Ae.utils.py.engine import Engine
from Ae.utils.py.share import ShareUtil
from Ae.constants.share import BASE_DIR

# Ae窗口最小化时找不到标题，导致程序阻塞，坑！
# ensure_app_started()

engine = Engine(version="18.0")
statements = []
share_util = ShareUtil(engine)
statements += share_util.head(BASE_DIR + '/基础/树/b-tree/conf.json')
statements += share_util.body()
statements += share_util.tail()
engine.execute('__main__', statements)
