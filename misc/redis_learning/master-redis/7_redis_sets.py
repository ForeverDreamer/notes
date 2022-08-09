from utils import *

cars = 'cars'

# print(sadd(cars, 'toyota', 'maserati', 'ford'))
# print(sadd(cars, 'mazda'))

# print(scard(cars))

# print(srem(cars, 'mazda'))
# print(srem(cars, 'toyota', 'maserati'))

# print(spop(cars))
# print(spop(cars, 2))

# print(smembers(cars))

# print(sismember(cars, 'mazda'))
# print(sismember(cars, 'maserati'))

# print(srandmember(cars))
# print(srandmember(cars, 2))


# 122. Moving elements within sets via SMOVE
src = 'src'
dst = 'dst'
# print(sadd(src, 'one', 'two', 'three'))
# print(sadd(dst, 'four', 'five', 'six'))
# print(smembers(src))
# print(smembers(dst))
#
# print(smove(src, dst, 'one'))
# print(smembers(src))
# print(smembers(dst))


# 124. Sets Operations
# print(sunion([src, dst]))
# print(sunion([src, dst, cars]))

# print(sunionstore('all', [src, dst, cars]))
# print(smembers('all'))

# print(sinter([cars, 'all']))
# print(sinter([src, 'all']))
# print(sinter([dst, 'all']))

# print(sinterstore('inter', [dst, 'all']))

print(smembers('all'))
print(smembers(cars))
print(smembers(src))
# 'all' - cars
print(sdiff(['all', cars]))
# 'all' - cars - src
print(sdiff(['all', cars, src]))

print(sdiffstore('diff', ['all', cars, src]))
