from functools import wraps


def cache(func):
    memory = {}

    @wraps(func)
    def wrapper(n):
        if n in memory:
            return memory[n]
        result = func(n)
        memory[n] = result
        return result

    wrapper.log = memory
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
