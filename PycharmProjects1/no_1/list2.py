#3.2 remove命令
numbers = ['0', '1', '2', '3', '13']
print(numbers)

dislike_number = '13'
numbers.remove(dislike_number)#remove将不清楚元素位置但是知道其内容的元素删除，与pop命令一样，将其从列表中删除时还可继续使用它的值，remove将只删除第一个指定的值，如果要删除的值有多个，将要使用循环。
print(numbers)
print("\nI realy dont like the number that is " + dislike_number + ".")

#对列表进行排序
table = ['Ab', 'Bc', 'DX', 'Cd']
table.sort()#sort()命令将列表中的元素以首字母的顺序排列，该项改动是永久性的
print(table)
table.sort(reverse=True)#给sort()命令传递参数reverse=True后，sort()命令将以与字母顺序相反的方向执行
print(table)
table1 = ['ak', 'ij', 'uh', 'pl']
print("Here is the original list:")
print(table1)
print("\nHere is the sorted list:")
print(sorted(table1,reverse=True))#sorted()命令可以暂时的改变列表的元素顺序，注意与sort()命令的区别，此处列出将参数传递给sorted()命令的用法
print("\nHere is the orignial again:")
print(table1)
##倒着打印列表
table1.reverse()#reverse()命令将列表中的元素倒着打印出来，此项排序是永久性的
print(table1)

##确定列表的长度
table1 = ['ak', 'ij', 'uh', 'pl']
print(len(table1))#在IDE中使用时要使用print()打印出来

