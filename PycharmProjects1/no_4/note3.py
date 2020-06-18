##元组（使用圆括号()来定义元组，元组中的元素是不能被修改的），访问修改元组中元素值的语法不变
dim = (200,40)
print(dim[0])
print(dim[1])
for number in dim:
    print(number)
print("Original dim:")
for number in dim:
    print(number)
dim = (240,80)
print("\nModified dim:")
for number in dim:
    print(number)
