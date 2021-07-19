class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(self.first_name + self.last_name)
    
class Admin(User):
    def __init__(self, first_last, last_name):
        super().__init__(first_last, last_name)
        self.privilegee = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
   
    def show_privileges(self):
        for privilege in self.privileges:
            print('The Admin has ' + privilege)
                
Admining = Admin('Liu', 'JinChen')

Admining.privilegee.show_privileges()