while True:
    a = input("Please enter a number:")
    b = input("Please enter another number:")
    if a == 'q' or b == 'q':#or关键字应连接两语句（在此处为判断是否为字符串'q'）
        break
    else:
        try:
            A = int(a)
            B = int(b)
        except ValueError:
            print("An string has been enter!")
        else:
            c = A + B
            print(c)
