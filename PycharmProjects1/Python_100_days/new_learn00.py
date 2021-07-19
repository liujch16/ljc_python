def factorial(num):
    '''求阶乘'''
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = input('m = ')
n = input('n = ')
print(factorial(m) // factorial(n) // factorial(m - n))
