class Employee():

    def __init__(self, first, last, payment):
        self.first = first
        self.last = last
        self.payment = payment

    def give_raise(self, payment_raise = ''):
        if payment_raise:
            self.payment += int(payment_raise)
        else:
            self.payment += 5000
    
    def print_current_payment(self):
        print(self.payment)

my_enter = Employee('Liu', 'Jin', 15000)
my_enter.give_raise(150000)
my_enter.print_current_payment()