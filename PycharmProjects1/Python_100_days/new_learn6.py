'''
输入两个正整数计算他们的最大公约数和最小公倍数

'''

num_1 = int(input('x = '))
num_2 = int(input('y = '))

if num_1 > num_2:
    num_1, num_2 = num_2, num_1

for factor in range(num_1, 0, -1):
    if num_1 % factor == 0 and num_2 % factor == 0:
        print('%d和%d的最大公约数是%d' % (num_1, num_2, factor))
        print('%d和%d的最小公倍数是%d' % (num_1, num_2, num_1 * num_2 // factor))
        break






