#6-5
'''创建一个字典，在其中存储三个键值对
   1.使用循环打印一个包含键与值的句子
   2.使用循环打印键
   3.使用循环打印值'''
nums = {'A': '1', 'B':'2', 'C':'3'}

##1
for Keys,Values in nums.items():
    print('The ' + Keys + ' runs through ' + Values)
##2
for Keys in nums.keys():
    print(Keys)
##3
for Values in nums.values():
    print(Values)