from shots.consts import CONF_PATH
from Ae.utils.py.engine import Engine
from Ae.utils.py.share import ShareUtil

engine = Engine(version="18.0")

statements = []
share_util = ShareUtil(engine)
statements += share_util.head(CONF_PATH)
statements += share_util.body()
statements += share_util.tail()
engine.execute('__main__', statements)
