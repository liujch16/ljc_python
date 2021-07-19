#PythonDraw(蟒蛇绘制).py
import turtle as t #将引用的库的名称更换以达到防止函数重名的情况发生
t.setup(650,350,200,200) #设定初始海龟的位置及窗体的长宽，(宽度，高度，起始点坐标x，y)
t.penup() #空笔命令，此时海龟不在画布上留下痕迹
t.fd(-250) #走直线，d为距离
t.pendown() #着笔命令，与空笔命令成对出现，效果相反
t.pensize(25) #将海龟的腰围设置为25个像素
t.pencolor("purple")
t.seth(-40) #方向控制函数，改变行进方向(绝对角度)
for i in range(4):#循环语句，range之后的参数为循环的次数，for in之间的变量表示每次循环的计数
    t.circle(40,80)#根据半径绘制角度的弧型，r为角度，ext为弧度，圆心默认在海龟左侧距离为r
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done() #运行完毕之后不会退出的一行代码