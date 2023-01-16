from ae.utils.py.engine import Engine
from ae.utils.py.share import ShareUtil

# Ae窗口最小化时找不到标题，导致程序阻塞，坑！
# ensure_app_started()

engine = Engine(version="18.0")
statements = []
share_util = ShareUtil(engine)
statements += share_util.head('基础/树/b-tree/conf.json')
statements += share_util.body()
statements += share_util.tail()
engine.execute('__main__', statements)
