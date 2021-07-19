def make_album(name, album, num = ' '):#为函数增加一个可选的形参
    if num:#当num不为空时bool值为True，执行if语句
        m_a = {'singer_name': name, 'album_name': album}#返回一个字典
    else:
        m_a = {'singer_name': name, 'album_name': album, 'num_1': num}
    return m_a

A_1 = make_album(name = '1', album = '2')
A_2 = make_album('3', '4', num = '100')
A_3 = make_album('5', '6')

print(A_1)
print(A_2)
print(A_3)