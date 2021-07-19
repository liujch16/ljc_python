def make_great(names1, Great_name):
    while names1:
        current_name = names1.pop()
        current = 'the Great ' + current_name
        Great_name.append(current)
    

'''
使用该函数打印列表中的元素
'''
def show_magition_name(names):
    for name in names:
        print("\nThere is one magition name's " + name)

magitions = ['jil', 'hik', 'fyn']
Great_name = []

make_great(magitions[:], Great_name)#向函数传递列表的副本来达到禁止函数修改列表的目的
show_magition_name(Great_name)
