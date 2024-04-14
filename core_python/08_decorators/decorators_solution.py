# Answer 1
import time

def timeer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds to run')
        return result
    return wrapper

@timeer
def example_function(n):
    time.sleep(n)
    
# example_function(2)

# Answer 2
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(a) for a in args)
        kwargs_value = ", ".join(f'{k}={v}' for k, v in kwargs.items())
        print(f'Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}')
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print('Hello')

@debug
def greet(name, greeting='Hello'):
    print(f'{greeting} {name}')
    
# hello()   
# greet("chai", greeting="Hi")

# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
# Answer 3

def cache(func):
    cached_value = {}
    # print(f'Cached value: {cached_value}')
    def wrapper(*args):
        print(f'Cached value: {cached_value}')        
        if args in cached_value:
            return cached_value[args]
        result = func(*args)
        cached_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(5)
    return a + b
print(long_running_function(1,2))
print(long_running_function(1,2))
print(long_running_function(1,5))
