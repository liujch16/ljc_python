'''
比较、逻辑和身份运算符的使用

'''

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = not (1 != 2)
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
'''
使用input()函数获取键盘的输入（字符串）
使用int()函数将输入的字符串转换为整数
使用print()函数输入带占位符的字符串

'''

'''

分段函数求值
      
       3x - 5 (x > 1)
f(x) = x + 2 (-1 <= x <= 1)
       5x + 3 (x < -1)

'''

x = float(input('x = '))
if x < -1:
    y = 5 * x + 3
elif x <= 1: 
    y = x + 2
else:
    y = 3 * x - 5
print('f(%.2f) = %.2f' % (x, y))# %作为占位符将x,y在print()语句中的位置确定，其后的2f表示输出时使用小数点后两位数字

