##接note1 列表解析
squares = [vaule**2 for vaule in range(1,30,2)]#首先指定一个列表名，指定一个表达式用于生成要储存的值，之后再接上一个for循环用于给表达式提供值
print(squares)
##使用列表的一部分
numbers = ['1', '2', '3', '4']
print(numbers[0:3])#将列表的前两个元素打印出来（缺一原理），数字中间使用冒号隔开！！！

numbers1 = ['6', '7', '8', '9', '0']
for number in numbers1[0:3]: #在遍历中使用循环，将列表中的部分元素进行遍历
    print(number)
##复制列表
letters1 = ['A', 'B', 'C', 'D']
letters2 = letters1[:]#制作一个不指定索引的切片，实现复制一个列表的效果，不能单纯的将一个列表赋值给另外一个，这样无法得到一个新列表
print(letters2)
letters2.append("F")
print("\nThese are some letters:")
print(letters1)
print("\nThese are more letters:")
print(letters2)
##
