# 方法2 (1*2*3*...*x)
def fct2(x):
    if x == 0:
        return 1
    else:
        return eval('*'.join(map(str, list(range(1, x + 1)))))


print('方法2: 50! =', fct2(50))
