from utils import *

name = 'dept'

# print(lpush(name, "Sales"))
# print(lpush(name, "Admin", "HR"))
# print(lrange(name, 0, -1))
# print(rpush(name, "Programming"))
print(lrange(name, 0, -1))
# print(lindex(name, 0))
# print(lindex(name, -1))
# print(linsert(name, 'before', "Admin", "Legal"))
# print(lrange(name, 0, -1))
# print(linsert(name, 'after', "Sales", "Social"))
# print(lrange(name, 0, -1))
# print(lpop(name))
# print(lrange(name, 0, -1))
# print(rpop(name))
# print(lrange(name, 0, -1))
# print(ltrim(name, 1, -1))
# print(lrange(name, 0, -1))
# print(lset(name, 2, 'Programming'))
# print(lrange(name, 0, -1))
print(llen(name))
print(lrem(name, 0, 'Sales'))
