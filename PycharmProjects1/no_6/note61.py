#字典
alien_0 = {'color': 'green', 'points':5}#字典用花括号，键和值都使用单引号
print(alien_0['color'])#指明键，程序即会输出对应的值

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")#从上述定义的字典获得与键"points"相关的值，将这个值存储在变量new_points中
#添加键——值对，依次指定字典名、用方括号起的键和相关联的值
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#先创建一个空的字典，再往里加入键值对
alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = '999'
print(alien_1['color'])
#删除键值对，使用del命令删除相应的键值对
del alien_1['color']
print(alien_1)
