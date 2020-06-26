#6-7
'''创建2⃣️个包含2⃣️个人信息的字典并将2⃣️个字典都储存到一个列表中，之后将其打印'''
per0 = {
    'name': 'liu',
    'points': '90',
    'school': 'Lanzhou uni'
    }
per1 = {
    'name': 'tian',
    'points': '80',
    'school': 'Lanzhou',
    }
pers = [per0,per1]

for per in pers:
    print('The name is ' + per['name'] +
          '\nThe points is ' + per['points'] +
          '\nThe school is ' + per['school'])

