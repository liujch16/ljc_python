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

for key, value in user_0.items():##编写用于遍历字典中的for循环，可声明两个变量，用于存储键值对.items()方法返回一个键值对列表，for循环依次将每个键值对存储到指定的两个变量中
    print("\nKey:" + key)##将键存储到key中，将值存储到value中
    print("Value: " + value)
##遍历字典中的所有键
for k in user_0.keys():##keys()命令让程序提取字典中的所有键，并依次将他们存储到变量中
    print('\n' + k + '.')

for k1 in user_0:##直接遍历字典时将会默认遍历字典中的所有键（.keys()的隐式）
    print('\n' + k1 + '.')
##使用当前键来访问与之相关的值
nums_0 = {'H': '9',
          'O': '8',
          'Y': '6',
          'I': '5',
          }

nums_1 = ['O','I']

for num_0 in nums_0.keys():
    print(num_0)
    if num_0 in nums_1:
        print(num_0 + ':' + 'WWWWhat?' +
              '\tya got a lucky number :' +
              nums_0[num_0] + '！！！')
##keys函数
if 'P' not in nums_0.keys():##keys()函数并非只能用于遍历中，事实上它返回了一个由字典中所有键组成的列表
    print('soooory~')