class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.value = 0
        self.value_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value_index + 1 > self.count:
            raise StopIteration
        value_to_return = self.value
        self.value_index += 1
        self.value += self.step
        return value_to_return


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)


# Решение на лекцията
class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.value_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value_index == self.count:
            raise StopIteration
        value_to_return = self.value_index * self.step
        self.value_index += 1
        return value_to_return
