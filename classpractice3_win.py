from collections import OrderedDict#从collections模块中导入了OrdereDict类，该类与字典的行为几乎相同，创建一个有序字典

favorite_language = OrderedDict()#创建一个OrderedDict实例

favorite_language['jens'] = 'python'
favorite_language['Liu'] = 'C++'

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + 
    language.title())