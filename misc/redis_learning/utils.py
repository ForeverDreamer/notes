import redis

r = redis.Redis(decode_responses=True)
# r = redis.Redis(host='127.0.0.1', port=6379)
# r = redis.Redis(host='hostname', port=port, password='password')


def set_key(k, v):
    r.set(k, v)


def get_key(k):
    return r.get(k)
