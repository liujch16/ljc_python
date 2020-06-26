lower = int(input("输入区间最小值"))
upper = int(input("输入区间最大值"))
flag=0
for num in range(lower,upper + 1):
    flag = 0
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                flag=1
                break
        if flag == 0:
            print(num)