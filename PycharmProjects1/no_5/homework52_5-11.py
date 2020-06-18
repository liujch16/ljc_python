#5-11
'''序数表示位置，如1st和2nd。大多数序数以th结尾，只有1、2和3例外。
   1.在一个列表中储存数字1～9。
   2.遍历这个列表
   3.在循环中使用一个if-elif-else结构，以打印每个数字对应的结尾
     。输出内容应为1st、2nd、3rd、4th等，每个序号独占一行'''
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if number == '1':
        print(number + 'st')
    elif number == '2':
        print(number + 'nd')
    elif number == '3':
        print(number + 'rd')
    else:
        print(number + 'th')