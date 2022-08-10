from utils import *

name = 'users:followers'

# print(zadd(name, {'adam': 10, 'scott': 20, 'amy': 30}))
# print(zrange(name, 0, -1))
# print(zrange(name, 0, -1, True))

# print(zrevrange(name, 0, -1))
# print(zrevrange(name, 0, -1, True))

# print(zincrby(name, 5, 'adam'))
# print(zrange(name, 0, -1, True))
# print(zincrby(name, -5, 'adam'))
# print(zrange(name, 0, -1, True))
# print(zincrby(name, 5, 'hans'))
print(zrange(name, 0, -1, True))

# print(zrank(name, 'hans'))
# print(zrank(name, 'adam'))
# print(zrank(name, 'scott'))
# print(zrank(name, 'amy'))

print(zrevrank(name, 'hans'))
print(zrevrank(name, 'adam'))
print(zrevrank(name, 'scott'))
print(zrevrank(name, 'amy'))
