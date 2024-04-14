class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# Answer: 3 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def describe_battery(self):
        return f"The battery size of the car is {self.battery_size} KWh."
    
my_tesla = ElectricCar("Tesla", "Model S", 85)
print(my_tesla.brand)
print(my_tesla.full_name())
