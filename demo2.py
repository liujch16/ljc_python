'''
向函数传递列表(调试)，将两个功能封装在两个函数当中，
'''

def print_models(unprrited_designs, completed_modles):
    '''
    打印每个未打印列表中的元素，将打印过的元素添加到完成打印列表中
    '''
    while unprrited_designs:
        current_design = unprrited_designs.pop()

        print('Printing model: ' + current_design)
        completed_modles.append(current_design)

def show_comleted(completed_models):
    '''
    显示每个打印好的模型
    '''
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

unprinted_desgins = ['iphone case', 'robot pendant', 'ddecahedron']
completed_models = []

print_models(unprinted_desgins, completed_models)
show_comleted(completed_models)

