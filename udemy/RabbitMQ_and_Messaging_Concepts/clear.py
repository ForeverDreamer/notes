from utilts import *

with get_channel() as channel:
    queue_clear(channel)
    exchange_clear(channel)
