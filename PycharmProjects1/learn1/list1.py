letters = ['A', 'B', 'C' , 'D']
message = letters[1]
print(letters[0].lower(),letters[2].upper())
print('\nmessage')#换行符只能对字符串起作用

numbers = ['0', '1', '2']
print(numbers)
numbers[2] = '9'
print(numbers)#变更列表中单个元素的值
letters.append('F')#append命令为列表新添加一个元素，无需再将列表的新值赋给列表
print(letters)

letters1 = []#可以创建一个空白列表，之后用append命令将想要添加的元素加进去
letters1.append('A')
letters1.append('B')
letters1.append('O')
print(letters1)

numbers1 = ['1', '2', '3', '8', '9']
print(numbers1)
numbers1.insert(3,'7')#insert命令将列表中指定的添加一个新空间，并将指定的元素添加进去，将其之后的元素右移一个位置
print(numbers1)
del numbers1[3]#del命令将指定位置的元素删除（在知道其位置索引的情况下）
print(numbers1)
poped_numbers1 = numbers1.pop()#pop（缺省位置）命令将列表最后一位元素删除，并且这个元素依然能够被访问，pop命令有两个作用
print(numbers1)
print(poped_numbers1)
print("My favourite number is " + poped_numbers1 + ".")
poped_numbers12 = numbers1.pop(0)#pop命令在括号中指定元素索引即可删除相应位置的元素
print("Her favourite number is " + poped_numbers12 + ".")

#2020.06.08