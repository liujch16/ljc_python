filename = 'programming_2.txt'

while True:
    user_name = input("Please enter your name, enter 'Q' to quit: ")
    if user_name == 'Q':
        break
    else:
        print("Greeting! " + user_name)
        with open(filename, 'a') as file_progect:
            file_progect.write(user_name + " has visited.\n")