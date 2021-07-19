def add(*args):#变量前的*符号表示该参数为一可变参数，缺省时返回0值
    total = 0
    for val in args:
        total += val
    return total
print(add())
print(add(1, 2))
print(add(1, 2 ,3))