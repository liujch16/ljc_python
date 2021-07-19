class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):#初始化Restaurant类的两个属性
        self.restaurant_name = restaurant_name#获取储存在形参中的值并将其关联到创建的实例中去
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + '.')
        print("\nThe restaurant's cuisinetype is " + self.cuisine_type + '.')
        
    def open_restaurant(self):
        print('\nThe restarant is running.')
        
restaurant = Restaurant('SHITANG', 'POI')
a_phenon_restaurant = Restaurant('YISHITANG', 'PO2')

restaurant.describe_restaurant()#调用类中的方法时，和调用函数一样需要添加括号
restaurant.open_restaurant()

a_phenon_restaurant.describe_restaurant()
    
        



