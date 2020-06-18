#5-8
'''创建一个至少包含5个用户名的列表，其中一个用户名为"admin"。
你要编写代码，在每位用户登陆网站之后都打印一条问候消息。遍历
用户列表，并向每位用户打印一条问候消息
1.如果用户名为"admin"，就打印一条特殊的问候消息，"Hello admin,
would you like to see a status report?"。
2.否则就打印一条普通的问候消息，"Hello Eric,thank you for logging in"'''
names = ["Admin", "Bug", "Lily", "keven", "Osias"]

for name in names:
    if name == "Admin":#遍历元素时大小写敏感
        print("Hello Admin,would you like to see a status report?")
    else:
        print("Hello " + name +"\tthank you for logging in")



