#5-10
'''1.创建一个至少包含5个用户名的列表，将其命名为users
   2.再创建一个包含5个用户名的列表，将其命名为new_users
     并确保其中有一两个用户名也包含在users中
   3.遍历列表new_users，对于其中的每个用户名，都检查其是否已经
     被使用。如果是这样，就打印一条消息，指出需要输入别的用户，否则，
     打印一条消息，指出这个用户名未被使用
   4.确保比较时不区分大小写'''
users = ['A', 'B', 'C', 'O', 'P', 'I']
new_users = ['A', 'N', 'i', 'U', 'l']
for new_user in new_users:
    new_user = new_user.upper()
    if new_user in users:
        print("Need another user's name!" + "\nDisabled name:" + new_user)
    else:
        print(new_user + "\thasnot been used.")