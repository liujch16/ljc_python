class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_describe_name(self):#规范化输出基本信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):#打印里程
        print("This car has " + str(self.odometer_reading) + "miles on it.")
        
    def update_odomter(self, milesage):#更新里程
        if milesage >= self.odometer_reading:
            self.odometer_reading = milesage
        else:
            print("You can't roll back an odemeter!")
            
    def incremetent_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def describe_battert(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def upgrate_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):#作为Car()父类的子类，继承了Car()的所有属性并添加了一个独有的属性self.battery，代码中通过一个单独的Battery()类来赋予
    def __init__(self, make, modle, year):
        super().__init__(make, modle, year)#super函数让ElectriCar实例包含父类的所有属性
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'modle s', 2016)

print(my_tesla.get_describe_name())
my_tesla.battery.describe_battert()#此行代码使Python在实例my_tesla中查找属性battery，并对储存在该属性的Battery实例调用方法describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrate_battery()
my_tesla.battery.get_range()





