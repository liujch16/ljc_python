#修改字典中的值，指定字典名、方括号中的键以及与键相关联的新值
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0['color'] = 'yellow'
print(alien_0['color'])
#另外一个例子
alien_1 = {'x_position': 0,'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_1['x_position']))

##向右移动，并以速度决定将移动多远
alien_1['speed'] = 'fast'
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment

print("New x_position: " + str(alien_1['x_position']))
