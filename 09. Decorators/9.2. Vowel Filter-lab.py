from functools import wraps


def vowel_filter(function):
    vowel = ['a', 'e', 'y', 'u', 'i', 'o']

    @wraps(function)
    def wrapper():
        result = function()
        return [x for x in result if x in vowel]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
