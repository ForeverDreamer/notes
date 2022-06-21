# SET <ip> 1 
# SET 10.10.10.234 1

# *3\r\n$3\r\nSET\r\n$10\r\n10.10.10.1\r\n$1\r\n1\r\n

# 1. Read the file 
# 2. data and convert into RESP syle conventions

import sys

def generate_resp(ips):

    # print (ips) 

    pattern = '*3\r\n$3\r\nSET\r\n${0}\r\n{1}\r\n$1\r\n1\r\n'

    for ip in ips:
        sys.stdout.write(pattern.format(len(ip), ip))

if __name__ == '__main__':

    data = ''

    with open('ips.txt', 'rt') as f:

        data = f.read()

    ips = data.split('\n')

    generate_resp(ips)


# 执行命令
# python block_ips.py | redis-cli --pipe

# 检查结果
# keys *
# get 10.10.10.1
# get 10.10.10.2
# get 10.10.10.3
# get 10.10.10.4