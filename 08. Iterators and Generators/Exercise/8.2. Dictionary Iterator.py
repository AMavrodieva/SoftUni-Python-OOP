# class dictionary_iter:
#     def __init__(self, dictionary: dict):
#         self.items = list(dictionary.items())
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.items):
#             raise StopIteration
#         current_value = self.items[self.index]
#         self.index += 1
#         return current_value


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
#
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)

# Второ решение
class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.generator = (pair for pair in self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)