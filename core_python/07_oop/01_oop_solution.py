class Car:
    def __init__(self,userbrand,usermodel):
        self.brand = userbrand
        self.model = usermodel

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

my_car1 = Car("Honda","Civic")
print(my_car1.brand)
print(my_car1.model)

