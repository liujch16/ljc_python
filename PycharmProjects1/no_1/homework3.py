#作业3-4、3-4、3-5、3-6、3-7

goust = ['A', 'B', 'C', 'D']
print(goust)
cannot_go = goust.pop(2)
print(cannot_go + "cannot join the party .")
goust.insert(2,'F')
print(goust)
print("I found a bigger table.")
goust.insert(0,'N')
goust.insert(2,'H')
goust.append('K')
print(" ".join(goust) + "\twill come to the party.")#jion命令将列表中的元素转化为字符串之后再进行输出。
print("There are only two people will be invited.")
goust.pop(6)
goust.pop(5)
goust.pop(4)
goust.pop(3)
goust.pop(2)
print(goust[0] + " will be invited.")
print(goust[1] + " will be invited.")
del goust[0]
del goust[1]
print(goust)

#2020.06.08