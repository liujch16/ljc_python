class Car():
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.read_odmettering = 0#在方法__init__()内直接指定某个属性的初始值时无需再为它提供厨师追的形参
    def get_descriptive(self):
        '''返回整洁的消息'''
        long_name = self.make + ' ' + self.modle + ' ' + str(self.year)
        return long_name.title()
    def read_odmetter(self):
        print("This car had " + str(self.read_odmettering) + " miles on it.")
    def upgratyed_odmetter(self, mileage):#通过添加新方法来更新属性，该方法通过接受一个新值，将该值存储在self.read_odmettering中
        if mileage >= self.read_odmettering:#对传递的新值进行判断检查读数是否合理
            self.read_odmettering = mileage
        else:
            print("You can't roll back an odmetter!") 
    
my_new_car = Car('audi', 'a4', 2017)
print(my_new_car.get_descriptive())
my_new_car.upgratyed_odmetter(23)#在此行代码中将23提供给方法upgrated_odmetter()，该实参对应于形参mileage
my_new_car.read_odmetter()








