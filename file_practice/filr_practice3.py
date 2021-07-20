filename = 'programming_1.txt'

with open(filename, 'w') as file_project:#向open()传递了两个参数，第一个参数是要打开的文件的名称
    #第二个实参('w')是要告诉python要以写入模式打开文件，若忽略模式实参python将以默认的只读模式打开
    #文件不存在时，open()将自动创建，以写入('w')模式打开文件时将在返回对象前清空该文件
    file_project.write("I love programming.\n")
    file_project.write("I also creating new games.\n")#写入多行时没有指定换行符时，txt文件内容会挤在一起
    