# SET <ip> 1 
# SET 10.10.10.234 1

# *3\r\n$3\r\nSET\r\n$10\r\n10.10.10.1\r\n$1\r\n1\r\n

# 1. Read the file 
# 2. data and convert into RESP syle conventions

import sys

PATTERN = '*3\r\n$3\r\nSET\r\n${0}\r\n{1}\r\n$1\r\n1\r\n'


if __name__ == '__main__':

    with open("ips.txt", "rt") as f1:
        ips = f1.readlines()
        # with open("resp.txt", "wt") as f2:
        #     for ip in ips:
        #         ip = ip.strip()
        #         f2.write(PATTERN.format(len(ip), ip))
        for ip in ips:
            ip = ip.strip()
            sys.stdout.write(PATTERN.format(len(ip), ip))

# 执行命令
# python block_ips.py | redis-cli --pipe

# 检查结果
# keys *
# get 10.10.10.1
# get 10.10.10.2
# get 10.10.10.3
# get 10.10.10.4
