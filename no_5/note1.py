#if语句
letters = ['A', 'B', 'c', 'O', 'p']
for letter in letters:
    if letter != 'O':#!=为不等符
        print(letter.upper())
    else:
        print(letter.lower())
##if else语句
age = 17
if age >= 18:
    print("You'r adult")
else:#if后的条件执行未通过将执行else后的操作
    print("Get out")
#not in 语句
letters1 = ['V', 'N', 'O']
letter0 = 'v'
if letter0 in letters1:
    print('U')
#if-elif-else结构，python将逐个检查结构中的代码块，遇到通过的条件测试之将会跳过其余的测试
age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 4
else:
    price = 9
print('Your shoud pay\t' + str(price) + "$.")

