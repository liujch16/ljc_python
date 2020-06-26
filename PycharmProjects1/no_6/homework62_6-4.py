#6-4
'''使用一段循环代遍历之前的代码中的键与值'''
infomation = {'first_name': 'Lau',
              'last_name': 'jinchen',
              'age': '21',
              'city': 'nanjing'
              }
##6-3代码 以上
for value,key in infomation.items():
    print('Value: ' + value)
    print('Key: ' + key)

infomation['first_name'] = 'Tian'
infomation['last_name'] = 'Yi'
infomation['age'] = '20'
infomation['city'] = "Xi'an"

for value,key in infomation.items():
    print('Value: ' + value +
          '\n' +
          'Key: ' + key)
