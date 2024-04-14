# Answer 1
def square(num):
    return num**2
# print(square(5))

# Answer 2
def sum_of_num(numOne,numTwo):
    return numOne + numTwo
# print(sum_of_num(5,6))

# Answer 3
def muultiply(x,y):
    return x * y
# print(muultiply('a',5))

# Answer 4
import math
def circle_stats(radius):
    circumference = 2*(math.pi)*radius
    area = (math.pi)*(radius)**2
    return area, circumference
a,c = circle_stats(5)
# print("Area: ",a,"Circumference: ",c)

# Answer 5
def greets(name="Gaurav"):
    return f"Hello {name}!"
# print(greets("John"))

# Answer 6
cube = lambda x: x**3
# print(cube(5))

# Answer 7
def sum_all(*args):
    # print(*args)
    # print(args)
    # for i in args:
    #     print(i*2)
    return sum(args)
# print(sum_all(1,2,3))

# Answer 8
def print_kwargs(**kwargs):
    print(f"Type of passed argument: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
# print_kwargs(name="John", age=25)

# Answer 9
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
# print(list(even_generator(10)))
# for i in even_generator(10):
#     print(i)

# Answer 10
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
# print(factorial(5))