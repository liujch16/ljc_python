'''
向函数传递参数
'''

from random import randint as rt


def roll_dices(n = 2):#摇骰子
    total = 0
    for i in range(n):
        total += rt(1, 6)
    return total

def add(*args):#*表示args为（数量）可变参数
    total = 0
    for val in args:
        total += val
    return total

print(roll_dices(9))
print(add())
print(add(1, 89))
print(add(1, 89 ,79 ,90))#调用add()函数时可传入0个至多个函数

