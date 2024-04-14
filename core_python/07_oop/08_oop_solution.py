# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car():
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1
    
    @property
    def model(self):
        return self.__model



my_car = Car("Toyota", "Corolla")
# my_car.model = "Camry" # This will raise an error because model is a read-only attribute
# print(my_car.model()) # This will print "Corolla" because model is a read-only attribute

print(my_car.model)