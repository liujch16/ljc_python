#while循环
currebt_num = 1

while currebt_num <= 9:
    print(currebt_num)
    currebt_num += 1
#让用户选择何时退出

promot = "\nTell me something, and I will reapet it back to you:"
promot += "\nEnter 'quit' to end the program. "
message = ""
while message !='quit':
    message = input(promot)
    if message != 'quit':
        print(message)