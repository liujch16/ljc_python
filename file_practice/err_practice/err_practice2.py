print("Give me two numbers, and I'll divide them.")
print("Enter 'q'to quit.")

while True:
    first_numbe = input("\nFIrst number: ")
    if first_numbe == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:#try()代码块放置于此起到了防止程序奔溃的作用，当除数为0时将执行except()代码块中的语句，此代码块只包含可能会出错的语句
        answer = int(first_numbe) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)#依赖于try()语句成功执行的代码应该放在else代码块中