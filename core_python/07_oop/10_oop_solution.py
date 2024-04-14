class Car():
    # total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # Car.total_cars += 1

class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine"
    

class ElectricCar(Battery, Engine ,Car):
    pass
    
my_tesla = ElectricCar("Tesla", "Model S")

print("My Tesla is a isinstance of Car: ", isinstance(my_tesla, Car))
print("My Tesla is a isinstance of Battery: ", isinstance(my_tesla, Battery))
print("My Tesla is a isinstance of Engine: ", isinstance(my_tesla, Engine))

print(my_tesla.battery_info())
print(my_tesla.engine_info())