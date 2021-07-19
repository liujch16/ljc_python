def make_great(names1):
    Great_name = []
    while names1:
        current_name = names1.pop()
        current = 'the Great' + current_name
        Great_name.append(current)
    return Great_name


'''
使用该函数打印列表中的元素
'''
def show_magition_name(names):
    for name in names:
        print("\nThere is one magition name's " + name)

magitions = ['jil', 'hik', 'fyn']

make_great(magitions)
show_magition_name(magitions)