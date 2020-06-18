#第四章 操作列表
letters = ['A', 'B', 'C']
for letter in letters:#for使程序每次将列表中的一个元素提取出来存储到变量letter中，然后进行打印
    print(letter)
    print(letter.lower() + ",that was a great letter.")#第二行print语句位于for循环的缩进位置，所以在执行循环时每次都会将同一个元素带入循环执行一遍
print("Every letter is a good letter.")

##数值列表
for number in range(1,8):#range命令生成了七个数字，从指定的数字1开始，到指定的数字8之前结束（7个数字）
    print(number)
numbers = list(range(1,8))#list命令将range()所产生的数组变成了列表，并在之后的orint语句输出
print(numbers)

even_numbers = list(range(1,11,2))
print(even_numbers)

##平方列表
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares1 = []
for value in range(1,100,2):
    squares1.append(value**2)#在这一步中省去了临时变量
print(squares1)
message = sum(squares1)#求和函数
print("列表中所有元素之和是" + str(message))
message = max(squares1)#max函数
print("列表中最大的元素是" + str(message))


