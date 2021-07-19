class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print("The user's first name is " + self.first_name + '.')
        
    def grett_user(self):
        print('Hi ' + self.last_name + '!')
        

a_person = User('Liu', 'JinChen')    

a_person.describe_user()
a_person.grett_user()    




