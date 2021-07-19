import json

def get_stored_usrname():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            usrname = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return usrname
    
def get_new_usrname():
    usrname = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(usrname, f_obj)
    return usrname

def greet_user():
    username = get_stored_usrname()
    if username:
        print("The stored name is , " + username + ".")
        Y_1 = input("Is the name is right? Please enter 'y' or 'n'")
        if Y_1 == 'y':
            print("Welcome! " + username + ".")
        else:
            username = get_new_usrname()
            print("Your new usrname is " + username + ".")
    else:
        username = get_new_usrname()
        print("We'll remember you when you come back, " + username + "!")
        
greet_user()