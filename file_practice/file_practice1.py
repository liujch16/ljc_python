file_path = 'D:\\pythonworkspace1\\vscode_python\\file_practice\\pi_digits.txt'

with open(file_path) as file_object:#open()接受要打开的文件名并返回一个表示文件的对象(变量file_object)，
    #关键字with使python在合适的时候关闭文件
    lines = file_object.readlines()

pi_string = ''#在此处定义了一个空字符串
for line in lines:
    pi_string += line.strip()#strip()方法删除每个line元素左边的换行符
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the Pi")
else:
    print("Your birthday does not appear in the Pi")
print(pi_string)
print(len(pi_string))
