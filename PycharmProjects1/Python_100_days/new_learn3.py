'''while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为Ture循环继续，表达式的值为False循环结束。
以下通过一个小游戏来了解如何使用while循环
'''
import random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('对了！')
        break
print('你总共猜对了%d次' % counter)
if counter > 7:
    print('VAN 蛋')