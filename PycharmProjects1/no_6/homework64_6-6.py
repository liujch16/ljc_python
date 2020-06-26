#6-6
'''在之前的程序中创建一个应该会接受调查的人员名单，其中有些人已经包含在字典中，有些人没有
遍历这个名单，对于已经参加调查的人，打印一条消息表示感谢。对于还未参加调查的人邀请他参加'''
favorite_languages = { 'jen': 'python',
                       'sarah': 'c',
                       'edward': 'ruby',
                       'phil': 'python',
                       }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

shouldbeinvited = ['jen', 'sarah', 'edward', 'liu', 'tian']
for value in shouldbeinvited:
    if value in favorite_languages.keys():
        print(value.title() + ' thanks for jion !')
    else:
        print(value.title() + ' you are invitesd !')