class Dog():
    def __init__(self, name, age):#类中的函数称为方法，将方法定义成了包含三个形参：self、name和age
        '''初始化属性name和age'''
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + ' is now sitting.')
    
    def roll_over(self):
        print(self.name.title() + 'rolled over!')

my_dog = Dog('CX0', 5)
your_dog = Dog('yeshiCX0', 7)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years old' + '.')
my_dog.sit

print("\nYour dog's name is " + your_dog.name + '.')
print("Your dog is " + str(your_dog.age) + ' years old' + '.')
your_dog.roll_over




