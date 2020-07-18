#7-4
'''编写一个循环，提示用户输入一系列的数字，并在用户输入quit时结束循环。每当用户输入一种数字时，都打印一条信息，说一个字符串加上这个数字
'''
promote = '请输入数字'
promote += '\n在输入"quit"之后结束'

message = input(promote)
while message != 'quit':
    print('你输入的数字是' + message + '.')


