#4-3、4-4、4-5、4-6、4-7、4-8、4-9
##用一个for循环打印数字1～20（含20）
for number in range(1,21):
    print(number)
##创建一个列表，其中包含数字1～1 000 0，再使用一个for循环将这些数字打印出来
##创建一个列表，其中包含数字1～1 000 0，再用min和max核实该列表是从1开始到1 000 0结束的。此外对这个列表调用sum函数进行求和
big_number = []
for number in range(1,11):
    big_number.append(number)
print(big_number)
message1 = max(big_number)
print(message1)
message2 = min(big_number)
print(message2)
message3 = sum(big_number)
print(message3)
##通过给函数range()指定第三个参数来创建一个列表，其中包含1～10的奇数，再通过一个for循环将这些奇数打印出来
numbers3 = list(range(1,20,2))
for number in numbers3:
    print(number)
##创建一个列表，其中包含3～30内能被3整除的数字；再使用一个for循环将其打印
numbers4 = []
for value in range(3,33,3):
    numbers4.append(value)
print(numbers4)
##将同一个数字乘三次方。其中包含前10个整数(即1～10)的立方，再使用一个for 循环将这些立方数都打印出来。
##使用列表解析生成包含前十个整数的立方
numbers7 = [value1**3 for value1 in range(1,11)]
print(numbers7)
