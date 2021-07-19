user_name = input("Please enter your name: ")

file_name = 'programming.txt'

with open(file_name, 'a') as file_project:
    file_project.write(user_name)