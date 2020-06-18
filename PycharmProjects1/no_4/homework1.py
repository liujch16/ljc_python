pizzas = ['A', 'B', 'C']
for pizza in pizzas:
    print("Id like to try " + pizza + ".")
print("All kind of pizza is dilicus.\n")
##4-10、4-11、4-12
##选择在本章编写的一个程序，在末尾添加几行代码，完成以下任务：1.打印信息"The first items in the list"，再使用切片来打印列表的前三个元素。
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print("The first three items in the list are:")
print(squares[:3])
#2.打印信息"Three items from the middle of the list are:",再使用切片来打印列表中间的三个元素。
print("\nThree items from the middle of the list are:")
print(squares[3:6])
#3.打印信息"The last three items in the list are:"，再使用切片来打印列表末尾的三个元素
print("\nThe last three items in the list are:")
print(squares[-3:])
##创建一个列表的副本并用for循环把它打印出来
numbers0 = []
for number in range(1,10):
    numbers0.append(number)
print("\n原始列表为：")
print(numbers0)
numbers1 = numbers0[:]
for number_1 in numbers1:
    print(number_1)
