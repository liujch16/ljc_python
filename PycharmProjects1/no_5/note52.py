#遍历之前检查列表是否为空
requesteed_toppings = []

if requesteed_toppings:
    for requested_toppong in requesteed_toppings:
        print("Adding " + requested_toppong + ".")
    print("\nYou are fired!")
else:
    print("You are fired too")#列表为空所以无输出
#检查多个列表
numbers1 = ['1', '2', '3', '4']

numbers2 = ['7', '8', '0']

for number1 in numbers1:
    if number1 in numbers2:
        print('There is a same number ' + number1 + '.')
    else:
        break
    print('There isnt any same number.')
print('\nNumberCheck is end.')