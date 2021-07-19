class Resuaurant():
    def __init__(self, type1, test):
        self.type = type1
        self.test = test
        self.number_served = 0
    def read_info(self):
        print(self.type1, self.test)
    def set_number_served(self, number):
        if number > 0:
            self.number_served = number
        else:
            print('The number is wrong!')
    def increment_number_served(self, increase_number):
        self.number_served += increase_number
    def print_numberinfo(self):
        print("There's " + str(our_resuarant.number_served) + ' eatting in the resuarant')

our_resuarant = Resuaurant('tiananmeng', 'good')

our_resuarant.set_number_served(80)
our_resuarant.increment_number_served(11)
our_resuarant.print_numberinfo()


