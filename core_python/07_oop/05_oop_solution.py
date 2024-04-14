
class Car():
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def describe_battery(self):
        return f"The battery size of the car is {self.battery_size} KWh."
        
    def fuel_type(self):
        return "Electricity"
    
my_car = Car("Toyota", "Corolla")
print("My Car:",my_car.fuel_type())

my_tesla = ElectricCar("Tesla", "Model S", 85)
print("My Tesla:",my_tesla.fuel_type())



