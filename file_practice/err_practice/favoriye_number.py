import json

filename = 'favorite_num.json'

try:
    with open(filename) as f_pbjj:
        num = json.load(f_pbjj)
except FileNotFoundError:
    num = input("Please enter your favorite number: ")
    with open(filename, 'w') as f_pbjj:
        json.dump(num, f_pbjj)
        print("Your favorite number is " + num)
else:
    print("We'll remember your number is " + num + ".")
    