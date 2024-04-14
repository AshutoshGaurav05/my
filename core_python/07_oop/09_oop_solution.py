class Car():
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def describe_battery(self):
        return f"The battery size of the car is {self.battery_size} KWh."
        
    def fuel_type(self):
        return "Electricity"

my_tesla = ElectricCar("Tesla", "Model S", 85)

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))