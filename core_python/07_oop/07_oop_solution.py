class Car():
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation." 


my_car = Car("Toyota", "Corolla")
# print("General Description:",my_car.general_description()) # This will raise an error because general_description is a class method and not an instance method
print("General Description:",Car.general_description())