#continue语句，返回到循环开头，根据条件测试结果判断是否继续循环
curren_num = 0
while curren_num < 10:
    curren_num += 1
    if curren_num % 2 == 0:
        continue#当if语句的条件为真时，程序执行continue语句，忽略余下的代码，并返回到循环的开头。否则将执行余下的代码

    print(curren_num)
#避免无限循环
