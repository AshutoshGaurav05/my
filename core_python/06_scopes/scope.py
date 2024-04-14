username = "ashutosh"
def func1():
    username = "gaurav"
    print(username)

# print(username)
# func1()

x = 100
def func2(y):
    z = y + x
    return z
# print(func2(5))

# def func4():
#     global x 
#     x = 50
# func4()
# print(x)


def f1():
    x = 80
    def f2():
        print(x)
    # f2()
    return f2

# result = f1()
# print(result)
# result()

def chaicode(num):
    def actual(x):
        return x ** num
    return actual
f = chaicode(4)
g = chaicode(3)

print(f)
print(g)

print(f(2))
print(g(5))