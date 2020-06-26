#嵌套
##字典列表
aliens = []

for nums in range(30):
    new_alien = {'color':'grey', 'points':'8', 'speed':'90'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('We got ' + str(len(aliens)) + ' aliens')

##列表字典
pizza ={
    'crust': 'thick',
    'toppings': ['mushrooms', 'extrs cheese'],
    }
print("You ordered a " + pizza['crust'] + '-crust pizza ' +
      "with the fpllpwing toppins:")

for topping in pizza['toppings']:
    print("\t" + topping)
###另外一个示例
nums = {
    'A': ['1', '2', '0'],
    'N': ['9','i'],
    'O': ['iop'],
    }

for Keys,Values in nums.items():
    if len(Values) > 1:
        for value in Values:
            print('We have more than one:' + value)
    else:
         element = ''.join(Values)
         print('We just got one:' + element)

##字典中的字典
users = {
    'Law': {
        'location': 'Xian',
        'points': '2',
        'favorite_number': '90'
    },
    'Tian': {
        'location': 'Beijin',
        'points': '3',
        'favorite_number': '80'
    },
}

for user,info in users.items():
    print("\nUser " + user)
    print("Location is " + info['location'])
    print("Favorite numbers is "+ info['favorite_number'])