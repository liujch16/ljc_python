import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)#使用.load()命令加载存储在numbers.json中的信息并存储在变量中

print(numbers)