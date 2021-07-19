#7-2
'''电影院将会根据年龄来收费，请编写一个循环，在其中询问用户的年龄，并指出票价(不到3岁的观众免费，3～12岁的观众为10美元
，超过12岁的观众为15美元)'''
custom_age = int(input('请输入您的年龄'))
promote = '\n您的票价为： '
price = ''
if custom_age < 3:
    price = 'free'
elif custom_age <= 12:
    price = '10'
else:
    price = '15'

print(promote + price)

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')





