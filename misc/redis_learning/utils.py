import redis

r = redis.Redis(decode_responses=True)
# r = redis.Redis(host='127.0.0.1', port=6379)
# r = redis.Redis(host='hostname', port=port, password='password')


# 2_getting_started
def ping():
    return r.ping()


def info(section=None):
    return r.info(section)


# 7_redis_sets
def sadd(name, *values):
    return r.sadd(name, *values)


def smembers(name):
    return r.smembers(name)


def scard(name):
    return r.scard(name)


def srem(name, *values):
    return r.srem(name, *values)


def spop(name, count=None):
    return r.spop(name, count)


def sismember(name, value):
    return r.sismember(name, value)


def srandmember(name, number=None):
    return r.srandmember(name, number)


def smove(src, dst, value):
    return r.smove(src, dst, value)


def sunion(keys, *args):
    return r.sunion(keys, *args)


def sunionstore(dest, keys, *args):
    return r.sunionstore(dest, keys, *args)


def sinter(keys, *args):
    return r.sinter(keys, *args)


def sinterstore(dest, keys, *args):
    return r.sinterstore(dest, keys, *args)


def sdiff(keys, *args):
    return r.sdiff(keys, *args)


def sdiffstore(dest, keys, *args):
    return r.sdiffstore(dest, keys, *args)


# 8_redis_sorted_sets
def zadd(name, mapping):
    return r.zadd(name, mapping)


def zrange(name, start, end, withscores=False):
    return r.zrange(name, start, end, withscores=withscores)


def zrevrange(name, start, end, withscores=False):
    return r.zrevrange(name, start, end, withscores=withscores)


def zincrby(name, amount, value):
    return r.zincrby(name, amount, value)


def zrank(name, value):
    return r.zrank(name, value)


def zrevrank(name, value):
    return r.zrevrank(name, value)


# 9_redis_hyperloglog
def pfadd(name, *values):
    return r.pfadd(name, *values)


def pfcount(*sources):
    return r.pfcount(*sources)


def pfmerge(dest, *sources):
    return r.pfmerge(dest, *sources)
