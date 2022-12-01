from functools import wraps
from os import sep


def store_results(func):

    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        with open(f'.{sep}result.txt', "a") as file:
            file.write(f'Function {func.__name__} was called. Result: {result}\n')

        return result

    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)

