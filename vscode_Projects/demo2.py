def A_full_name(name, album):
    full_name = name + ' ' + album 
    return full_name

while True:
    print('Please enter A name:')
    print("\nAnytime you enter a 'o' we will exit!")
    
    n_name = input('Name')
    if n_name == 'o':
        break
    
    a_name = input('Album')
    if a_name == 'o':
        break
    
    F_N = A_full_name(n_name, a_name)
    print('\nThis is your Album:' + F_N)