class Car():
    def __init__(self, years, modle, make):
        self.years = years
        self.modle = modle
        self.make = make
        self.odmetter_read = 0
    def info_reading(self):#规范化读取属性并输出
        print(str(self.years) + ' ' + self.modle + ' ' +self.make)
    def read_odmettering(self):#读取里程并输出
        print('This car has ' + str(self.odmetter_read) + ' miles!')
    def upgrated_odmetter(self, mileahgs):#更新里程
        if self.odmetter_read <= mileahgs:
            self.odmetter_read = mileahgs
        else:
            print("It's a useless data!")
    def increment_odmetter(self, miles):#为里程数增加相应的值
        '''将里程属性增加指定的值'''
        self.odmetter_read += miles
        
my_used_car = Car(90, 'outback', 'subaru')
my_used_car.info_reading()
my_used_car.upgrated_odmetter(23500)
my_used_car.read_odmettering()
my_used_car.increment_odmetter(100)
my_used_car.read_odmettering()


        
        
        
