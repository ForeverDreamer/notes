import redis

# 生成1百万个Key
# debug populate 1000000

# variables
file = 'allkeys_values.txt'
url = 'redis://localhost:6379'
query = '*'  # you can define any pattern '*name' 'key:??'

print('Reading keys...', end='')

client = redis.StrictRedis.from_url(url, decode_responses=True)
keys = client.keys(query)  # KEYS *

print(f'{len(keys):,} keys found.')


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# partitions = list(chunks(keys, 10000))


with open(file, 'w', newline='\n', encoding='utf-8') as f:
    total = len(keys) // 10000
    count = 1
    # for i in range(0, len(partitions)):
    for chunk in chunks(keys, 10000):
        # progress = ((i + 1) / len(partitions)) * 100
        progress = (count / total) * 100
        print(f'\rProcessing values... {progress:.2f}%', end='')
        # keys = partitions[i]
        keys = chunk
        values = client.mget(keys)
        for k, v in zip(keys, values):
            f.write(k)
            f.write('\n')
            f.write(v)
            f.write('\n')
        count += 1

print('\nProcessing Done....')
