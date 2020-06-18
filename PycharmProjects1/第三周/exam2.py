#天天向上(1).py
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown),"千分之一")
#天天向上(2).py
dayfactor = 0.005#引入变量dayfactor以方便修改参数
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown),"千分之五")
#天天向上(3).py
dayup = 1.0
dayfactor = 0.01
for i in range(365):#判断日期数是否对应了周末以实现模拟365天的自动化过程
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量:{:.2f}".format(dayup))
#天天向上(4).py
def dayUp(df):#定义函数dayUp，df作为dayfactor的简写在此处作为dayUp函数的参数，在接下来的程序编写中也能继续使用
    dayup = 1#赋值初始值为1
    for i in range(365):
        if i % 7 in[6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup#return语句是一个将dayup返回给主函数的语句，在此处作用为将dayup参数返回给while循环的作用，在将下来的学习中需要多注意函数返回值的使用
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001# "+=" 符号是加等号 ，c += a 等效于 c = c + a
print("工作日的努力参数是:{:.3f}".format(dayfactor))




