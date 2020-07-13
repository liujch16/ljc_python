#使用while获得一个计数chengxv
current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1
#标志
promot = "\nTell me something, and I will reapet it back to you:"
promot += "\nEnter 'quit' to end the program. "

active = True#选择一个标志作为检查的变量，用于判断整个程序是否处于活动状态，将程序设计为在标志为Ture时运行
while active:#当标志为Ture时循环将自动运行
    message = input(promot)
    if message == 'quit':
        active = False
    else:
        print(message)
#break语句  使用break语句立即退出循环，此时将不再管条件测试的结果如何，也不再运行余下的代码
