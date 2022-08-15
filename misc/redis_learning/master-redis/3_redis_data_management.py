from pprint import pprint as pp

from utils import *

# pp(kset('name', "Adnan"))
# pp(kset('fname', "Adnan"))
# pp(get('name'))
# pp(delete('name', 'fname'))
# pp(exists('name'))
# pp(exists('name', 'fname'))

# pp(kset('key1', 'value1', ex=120))
# pp(ttl('key1'))

# pp(expire('key1', 10))
# pp(ttl('key1'))
# pp(get('key1'))

# pp(kset('key1', 'value1', px=100000))
# pp(pttl('key1'))

# pp(pexpire('key1', 30000))
# pp(ttl('key1'))
# pp(pttl('key1'))
# pp(get('key1'))

# pp(persist('key1'))
# -1: 永不过期, -2: 过期, 正整数: 过期倒计时
# pp(ttl('key1'))
# pp(pttl('key1'))

# redis-py处于线程没有实现SELECT命令
# However, there is one caveat: the Redis SELECT command. The SELECT command allows you to switch the database currently in use by the connection. That database remains selected until another is selected or until the connection is closed. This creates an issue in that connections could be returned to the pool that are connected to a different database.
# As a result, redis-py does not implement the SELECT command on client instances. If you use multiple Redis databases within the same application, you should create a separate client instance (and possibly a separate connection pool) for each database.
# It is not safe to pass PubSub or Pipeline objects between threads.

# pp(keys())
# pp(flushdb())
# pp(keys())

# pp(rename('name', 'fname'))
# pp(keys())
# pp(renamenx('fname', 'name'))
# pp(renamenx('name', 'fname'))
# pp(keys())
# pp(renamenx('name', 'name1'))
# pp(keys())

# pp(ktype('fname'))

pp(unlink('name1', 'fname'))
pp(keys())
