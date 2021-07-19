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