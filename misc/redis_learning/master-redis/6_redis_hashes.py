from utils import *

name = 'user:101'

# print(hset(name, mapping={'fname': 'John', 'lname': 'Doe'}))
# print(hset(name, mapping={'k1': 'v1', 'k2': 'v2'}))
# print(hget(name, 'k1'))
# print(hgetall(name))
# print(hmget(name, ['k1', 'k2']))
# print(hlen(name))
# print(hdel(name, 'k1', 'k2'))
# print(hexists(name, 'k1'))
# print(hexists(name, 'fname'))
# print(hkeys(name))
# print(hvals(name))
# print(hset(name, 'score', 10))
# print(hincrby(name, 'score'))
# print(hset(name, 'commission', 0.25))
# print(hincrbyfloat(name, 'commission'))
print(hsetnx(name, 'myscore', 2.0))