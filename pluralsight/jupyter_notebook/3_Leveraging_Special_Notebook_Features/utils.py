import random
import string

def random_password(length):
    return ''.join(random.choices(string.ascii_letters, k=length))
