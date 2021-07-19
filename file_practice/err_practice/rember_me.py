import json 

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)#调用json.dump()，将用户名和一个文件对象传递给它从而将用户名存储到文件中
    print("We'll remember you when you come back, " + username + "!") 