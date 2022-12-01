from time import time
from functools import wraps
from os import sep


def exec_time(func):
    @wraps(func)
    def wrapper(*args):
        start = time()
        result = func(*args)
        end = time()

        with open(f'.{sep}result_execution', 'a') as file:
            file.write(f'Function {func.__name__} was called with {args}. Result is: {result} Elapsed time: {start-end}\n')
        return result
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total

print(loop(1, 10000000))


# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
#
#
# print(concatenate(["a" for i in range(1000000)]))
#
#
# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
#
#
# print(loop())
