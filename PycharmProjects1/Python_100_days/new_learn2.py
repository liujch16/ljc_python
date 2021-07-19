import math
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    reult = math.sqrt(dsquared)
    return reult
x1 = float(input('请输入第一个点的横坐标'))
y1 = float(input('请输入第一个点的纵坐标'))
x2 = float(input('请输入第二个点的横坐标'))
y2 = float(input('请输入第二个点的纵坐标'))

Distance = distance(x1, y1, x2, y2)

print('\n两点之间的距离为' + Distance)