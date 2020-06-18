#if语句
letters = ['A', 'B', 'c', 'O', 'p']
for letter in letters:
    if letter != 'O':#!=为不等符
        print(letter.upper())
    else:
        print(letter.lower())

age = 17
if age >= 18:
    print("You'r adult")
else:
    print("Get out")

letters1 = ['V', 'N', 'O']
letter0 = 'v'
if letter0 in letters1:
    print('U')

age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 4
else:
    price = 9
print('Your shoud pay\t' + str(price) + "$.")
#for循环与判断
requerted_toppongs = ['A', 'B', 'U']

for requerted_toppong in requerted_toppongs:
    print("Adding " + requerted_toppong + ".")
print("F")


