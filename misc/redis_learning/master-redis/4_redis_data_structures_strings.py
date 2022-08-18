from pprint import pprint as pp

from utils import *

name = 'student:101:score:math'

# pp(kset(name, 10))
pp(kset('json_key', '{"fname" : "John", "lname" : "Doe"}'))
# pp(incr(name))
# pp(incrby(name, 3))
# pp(decr(name))
# pp(decrby(name, 3))
# pp(incrbyfloat(name, 0.3))
# pp(incrbyfloat(name, -0.5))
# pp(strlen(name))
# pp(mset({'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}))
# pp(mget(['k1'], 'k2', 'k3'))
# 全部key都不存在才会成功
# pp(msetnx({'k6': 'v10', 'k5': 'v50', 'k4': 'v4'}))
# pp(getset('k1', 'v111'))
# pp(getrange('k1', 0, 2))
# pp(getrange('k1', -3, -1))
# pp(setrange('k1', 1, '666'))
# pp(setex('k1', 100, 'v100'))
# pp(psetex('k1', 30000, 'v30000'))
# pp(setnx('k10', 'v10'))
# pp(kobject('encoding', 'k10'))
# pp(scan())
# pp(scan(44, count=15))
# pp(scan(44, match='*:2*', count=15))
# pp(scan(44, match='*:2*', count=15, _type='string'))
pp(scan(44, match='*:2*', count=15, _type='zset'))
