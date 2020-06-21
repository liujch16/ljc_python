#按顺序遍历字典
nums_0 = {
    'abc': '123',
    'bcd': '234',
    'cde': '345',
    'uio': '456'
    }

for num_0 in sorted(nums_0.keys()):
    print(num_0)##调用函数sorted()keys()函数返回的列表按首字母排序后遍历
##遍历字典中的所有值
for num_0 in nums_0.values():##values()函数返回一个由字典中所有值所组成的列表，之后使用for语句遍历
    print('you got some number: ' + num_0)
##set()函数
nums_1 = {
    'xiaotian': '111',
    'xiaoliu': '222',
    'xiaotianya': '223',
    'xiaoliuya': '111',
    }

for num_1 in set(nums_1.values()):##set()函数将列表中重复的元素剔除
    print('\nOur favorite num is: ' + num_1)
