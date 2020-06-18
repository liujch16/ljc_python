#5-9
'''在5-8的练习中，添加一条if语句，检查用户列表是否为空
1.为空则打印消息"We need to find some users!"
2.删除列表中的所有用户名，确定将打印正确的消息'''
names1 = ["Admin", "Bog", "Lily", "keven", "Osias"]
names2 = ["Admin", "Bog", "Lily", "keven", "Osias"]
for name in names1:#使用遍历来删除列表中的元素时，由于remove命令在删除一个元素之后会将原索引数大于被删除的元素的元素的索引前进一位，所以会在删除操作时将被删除的元素之后的那个元素跳过
    if name in names1:
        names2.remove(name)
if names2:#在if语句中将列表名用在条件表达式中，Python将在列表至少包含一个元素时返回Ture，否则为False，执行else代码块
    for name in names2:
        if name == "Admin":
            print("Hello Admin,would you like to see a status report?")
        else:
            print("Hello " + name +"\tthank you for logging in")
else:
    print("We need find some users!")
