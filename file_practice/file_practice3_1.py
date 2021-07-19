filename = 'programming_1.txt'

with open(filename, 'a') as file_progrect:#向open()传递参数'a'，以附加模式打开文件，python不会在
    #返回文件对象前清空文件，写入有文件的行都将添加到文件末尾
    file_progrect.write("I also love finding meaning in large datesets.\n") 