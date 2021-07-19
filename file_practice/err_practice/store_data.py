import json#导入模块json

numbers = [2, 3, 4, 5, 6, 78]

filename = 'numbers.json'#创建.json文件来指出文件存储的数据为JSON格式
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)#使用函数json.dump()将数字列表存储到文件f_obj.json中