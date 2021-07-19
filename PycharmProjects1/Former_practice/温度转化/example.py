#Texample.py
TempStr=input("请输入带有符号的温度值：") #TempStr保存用户输入的信息，输入的信息以字符串类型保存在变量中
if TempStr[-1] in ['F','f']:#['F','f']列表类型，保留字"in"用于判断元素的存在与否
    C = (eval( TempStr[0:-1] ) - 32 )/1.8 #TempStr[0:-1]表示从字符串的第一个元素到最后元素之前的一个元素
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))#format是一个将F元素格式化的函数，大括号是一个将格式化后的F填充的槽、
else:
    print("输入格式错误")
