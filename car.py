
"""覆盖上一个car.py文件"""
class Car():
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()    
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, miles):  
        if miles >= self.odometer_reading:   
            self.odometer_reading = miles
        else:
            print("You can't roll back the odometer.")
          
    def increment_odometer(self, miles_increment):
        if miles_increment >= 0:
            self.odometer_reading += miles_increment   
        else:
            print("You can't roll back the odometer.")

            
# 定义类Battery()作为ElectricCar()类的属性
class Battery():
    
    def __init__(self): 
        self.battery_size = 70
        
    def describe_battery(self, size=''):
        if size:
            self.battery_size = size
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        else:
            range = (self.battery_size - 75)*1 + 240
        msg = "This car can go approximately " + str(range)
        msg += " miles on full range."
        print(msg)

        
class ElectricCar(Car):   
    
    def __init__(self, make, model, year):    
        """初始化父类属性"""
        super().__init__(make, model, year)   
        self.battery = Battery()