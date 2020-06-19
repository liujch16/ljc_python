#由类似对象组成的字典
nums = {
    'A': '1',##注意缩进的空格数为4
    'B': '2',
    'c': '3',
    }
print('The most favorite num is ' +
      nums['A'])##将较长的print语句分行的做法为：在第一行的末尾加上一个拼接运算符，同时注意一个tab（4个空格）的缩进对其
#遍历字典
user_0 = {
    'usersname': 'effect',
    'first': 'enrico',
    'last': 'fermi'
    }

for key, value in user_0.items():##编写用于遍历字典中的for循环，可声明两个变量，用于存储键值对
    print("\nKey:" + key)
    print("Value: " + value)