import json 

def greet_user():
    '''若用户存储了用户名就获取它'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj: 
            username = json.load(f_obj)
    except FileNotFoundError:#若json文件不存在就创建一个新的json文件并提示用户输入用户名
        username = input("Please enter your name: ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember your when you came back, " + 
                username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()