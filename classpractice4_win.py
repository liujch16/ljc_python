from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        a = randint(1, self.sides)
        print("This roll's result is " + str(a))

die_1 = Die()
i_1 = 0
while i_1 < 10:
    i_1 += 1
    die_1.roll_die()
    print('The sides of this die is ' + str(die_1.sides) + 
    ' The rolling number is ' + str(i_1))

die_2 = Die()
die_2.sides = 10
i_2 = 0
while i_2 < 10:
    i_2 += 1
    die_2.roll_die()
    print('The sides of this die is ' + str(die_2.sides))
