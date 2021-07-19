file_path = 'D:\\pythonworkspace1\\vscode_python\\file_practice\\learning_python.txt'

with open(file_path) as file_project:
    lines = file_project.readlines()

str_1 = ''
for line in lines:
    line = line.replace('Python', 'C')
    str_1 += line

print(str_1)
