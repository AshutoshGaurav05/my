class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def describe_battery(self):
        return f"The battery size of the car is {self.battery_size} KWh."
        
    
my_tesla = ElectricCar("Tesla", "Model S", 85)
# print(my_tesla.__brand) # This will give an error because __brand is a private variable
print(my_tesla.get_brand())
