from random import randint


def roll_dice(n=2):
    '''摇骰子'''
    total =  0
    for _ in range(n):
        total += randint(1, 6)
    return total

print(roll_dice(100))#摇100颗骰子