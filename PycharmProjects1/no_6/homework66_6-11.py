#6-11
'''创建一个字典，使用三个元素名作为键，对于每个元素都创建一个字典，其中包含与这个元素相关的三个元素作为值，将其打印'''
hobbies = {
    'football':{
        'date': 'today',
        'cost': 'many',
        'willdo': 'always',
    },
    'swim':{
        'date': 'last year',
        'cost': 'a few',
        'willdo': 'will',
    },
    'game':{
        'date': 'last month',
        'cost': 'None',
        'willdo': 'will',
    },
}

for hobbiy,detil in hobbies.items():
    print('\nI have such hobbies: ' + hobbiy)
    Date,Cost,Willdo = detil['date'],detil['cost'],detil['willdo']
    print("These are my hobbie's detils "+ '\n' + Date + '\n' +Cost + '\n' +Willdo)