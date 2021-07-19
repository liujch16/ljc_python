'''
输入一个数判断其是否为素数
'''

from math import sqrt

num = int(input('请输入一个整数：'))
end = int(sqrt(num))
is_prinme = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prinme = False
        break
if is_prinme and num != 1:#if语句判断中加入一个bool值时当且仅当bool值为True时判断为正
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
