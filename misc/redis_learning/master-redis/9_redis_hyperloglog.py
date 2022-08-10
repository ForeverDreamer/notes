from utils import *

main_page = 'visitors:main_page'
stocks = 'visitors:stocks'
company = 'visitors:company'
total = 'visitors:total'

# print(pfadd(main_page, 1, 2, 2, 4, 5))
# print(pfadd(stocks, 3, 4, 5, 5, 6, 7))
# print(pfadd(company, 6, 6, 7, 8))
#
# print(pfcount(main_page))
# print(pfcount(stocks))
# print(pfcount(company))
# 计算去重后的结果
# print(pfcount(main_page, stocks, company))

# 去重合并
print(pfmerge(total, main_page, stocks, company))
print(pfcount(total))
