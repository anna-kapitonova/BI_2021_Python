import time
import random
import requests


# 1. Write a simple decorator, that changes the output to the working time. (3 points)

def measure_time(func):
    def inner_function(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return (end - start)
    return inner_function


# 2. Create a decorator, that can log function launches,
# printing input and the type of output values. (7 points)

def function_logging(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} is called with", end=" ")

        if len(args) == 0 and len(kwargs) == 0:
            print("no arguments", end="")
        elif len(args) != 0:
            print("positional arguments: " + str(args), end="")
            if len(kwargs) != 0:
                print(" and ", end="")

        if len(kwargs) != 0:
            print("keyword arguments: "
                  + ", ".join([(str(key) + "=" + str(value)) for key, value in kwargs.items()]),
                  end="")

        print("\n", end="")
        print(f"Function {func.__name__} returns output of type {type(result).__name__}")

        return result
    return inner_function


# 3. Create a decorator "russian roulette",
# that returns decorator's input instead of function's output
# (with defined probability). (7 points)

def russian_roulette_decorator(probability, return_value):
    def inner_decorator(func):
        def inner_function(*args, **kwargs):
            result = func(*args, **kwargs)
            if random.random() > probability:
                return result
            else:
                return return_value
        return inner_function
    return inner_decorator


# Usage example

if __name__ == "__main__":

    print('Example usage: decorator "measure_time"')

    @measure_time
    def some_function(a, b, c, d, e=0, f=2, g="3"):
        time.sleep(a)
        time.sleep(b)
        time.sleep(c)
        time.sleep(d)
        time.sleep(e)
        time.sleep(f)
        return g

    print("For function some_function(1, 2, 3, 4, e=5, f=6, g='99999') the result is")
    print(some_function(1, 2, 3, 4, e=5, f=6, g="99999"), end="\n\n")

    print('Example usage: decorator "function_logging"')

    @function_logging
    def func1():
        return set()

    @function_logging
    def func2(a, b, c):
        return (a + b) / c

    @function_logging
    def func3(a, b, c, d=4):
        return [a + b * c] * d

    @function_logging
    def func4(a=None, b=None):
        return {a: b}

    print(func1(), end="\n\n")
    print(func2(1, 2, 3), end="\n\n")
    print(func3(1, 2, c=3, d=2), end="\n\n")
    print(func4(a=None, b=float("-inf")), end="\n\n")

    print('Example usage: decorator "russian_roulette_decorator"', end="\n\n")

    @russian_roulette_decorator(probability=0.2,
                                return_value="Ooops, your output has been stolen!")
    def make_request(url):
        return requests.get(url)

    print('For the following code:', end="\n\n")

    print("@russian_roulette_decorator(probability=0.2, ", end="")
    print("return_value='Ooops, your output has been stolen!'")
    print("def make_request(url):")
    print("    return requests.get(url))", end="\n\n")

    print("for _ in range(10):")
    print('    print(make_request("https://google.com")))', end="\n\n")

    print("The result is:")
    for _ in range(10):
        print(make_request("https://google.com"))
