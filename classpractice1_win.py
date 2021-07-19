class Car():#1 创建父类时，父类包含在当前文件中，且位于子类前面
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_desciriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    
    def read_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery = battery_size

    def describr_battery(self):
        print("This car has a " + self.battery + "-kWh battery.")

class ElectricCar(Car):#2 定义子类时，必须在括号里指定父类的**名称**

    def __init__(self, make, model, year):#3 方法__init__()接受创建Car示例所需的信息
        super().__init__(make, model, year)#4 此行代码调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性
        self.battery = Battery()# 此行代码将创建一个新的Battery实例，并将该实例存储在属性self.battery中。每当方法__init__()被调用时，都将执行该操作
    
my_tesla = ElectricCar('tesla', 'modle s', 2016)#5
print(my_tesla.get_desciriptive_name())
my_tesla.describe_battery()