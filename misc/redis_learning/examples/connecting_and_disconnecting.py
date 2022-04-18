import asyncio
import asyncio_redis


# The Connection class
async def connection_class():
    # Create Redis connection
    connection = await asyncio_redis.Connection.create(host='localhost', port=6379)
    # Set a key
    await connection.set('my_key', 'my_value')
    # When finished, close the connection.
    connection.close()


async def connection_pooling():
    # Create Redis connection
    connection = await asyncio_redis.Pool.create(host='localhost', port=6379, poolsize=10)
    # Set a key
    await connection.set('my_key', 'my_value')
    # When finished, close the connection pool.
    connection.close()


async def transactions():
    # Create Redis connection
    connection = await asyncio_redis.Pool.create(host='localhost', port=6379, poolsize=10)
    # Create transaction
    t = await connection.multi()
    # Run commands in transaction (they return future objects)
    f1 = await t.set('key', 'value')
    f2 = await t.set('another_key', 'another_value')
    # Commit transaction
    await t.exec()
    # Retrieve results
    result1 = await f1
    result2 = await f2
    print(result1, result2)
    # When finished, close the connection pool.
    connection.close()


async def pubsub():
    # Create connection
    connection = await asyncio_redis.Connection.create(host='localhost', port=6379)
    # Create subscriber.
    subscriber = await connection.start_subscribe()
    # Subscribe to channel.
    await subscriber.subscribe(['our-channel'])
    # Inside a while loop, wait for incoming events.
    count = 0
    while count < 3:
        reply = await subscriber.next_published()
        print('Received: ', repr(reply.value), 'on channel', reply.channel)
        count += 1
    # When finished, close the connection.
    connection.close()


code = """
local value = redis.call('GET', KEYS[1])
value = tonumber(value)
return value * ARGV[1]
"""


async def lua_scripting():
    connection = await asyncio_redis.Connection.create(host='localhost', port=6379)
    # Set a key
    await connection.set('my_key', '2')
    # Register script
    multiply = await connection.register_script(code)
    # Run script
    script_reply = await multiply.run(keys=['my_key'], args=['5'])
    result = await script_reply.return_value()
    print(result)  # prints 2 * 5
    # When finished, close the connection.
    connection.close()


from asyncio_redis.encoders import BytesEncoder


async def raw_bytes_or_utf_8():
    # Create Redis connection
    connection = await asyncio_redis.Connection.create(host='localhost', port=6379, encoder=BytesEncoder())
    # Set a key
    await connection.set(b'my_key', b'my_value')
    # When finished, close the connection.
    connection.close()


async def scanning_for_keys():
    # Create Redis connection
    connection = await asyncio_redis.Connection.create(host='localhost', port=6379, encoder=BytesEncoder())
    cursor = await connection.scan(match=b'*')
    while True:
        item = await cursor.fetchone()
        if item is None:
            break
        else:
            print(item)


# The RedisProtocol class
# @asyncio.coroutine
# def example():
#     loop = asyncio.get_event_loop()
#
#     # Create Redis connection
#     transport, protocol = yield from loop.create_connection(
#                 asyncio_redis.RedisProtocol, 'localhost', 6379)
#
#     # Set a key
#     yield from protocol.set('my_key', 'my_value')
#
#     # Get a key
#     result = yield from protocol.get('my_key')
#     print(result)
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(example())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(the_redisprotocol_class())
