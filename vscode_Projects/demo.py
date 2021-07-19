'''
学习传递信息
'''
#对于使用可选参数向结果返回可变元素字典的情况还需继续关注
def make_album(name, album, num = ' '):#为函数增加一个可选的形参
    if num:#当num不为空时bool值为True，执行if语句
        m_a = {'singer_name': name, 'album_name': album, 'num_1': num }#返回一个字典
    else:
        m_a = {'singer_name': name, 'album_name': album}
    return m_a

A_1 = make_album('1', '2')
A_2 = make_album('3', '4', num = '0')
A_3 = make_album('5', '6', '89')

print(A_1)
print(A_2)
print(A_3)