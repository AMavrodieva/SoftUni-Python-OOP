class reverse_iter_1:
    def __init__(self, value):
        self.value = list(value)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < - len(self.value):
            raise StopIteration
        return_value = self.value[self.index]
        self.index -= 1
        return return_value


class reverse_iter_2:
    def __init__(self, values):
        self.values = list(values)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.values):
            raise StopIteration

        value_to_return = self.values[self.index]
        self.index -= 1
        return value_to_return


class reverse_iter:
    def __init__(self, values):
        self.values = reversed(values)

    def __iter__(self):
        return iter(self.values)

#
reversed_list = reverse_iter_1([1, 2, 3, 4])
for item in reversed_list:
    print(item)
reversed_list = reverse_iter_2([1, 2, 3, 4])
for item in reversed_list:
    print(item)
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


# import unittest
#
# class ReverseIterTests(unittest.TestCase):
#     def test_zero(self):
#         res = ""
#         reversed_list = reverse_iter([1, 2, 3, 4])
#         for item in reversed_list:
#             res += str(item) + "\n"
#         self.assertEqual(res, "4\n3\n2\n1\n")
#
# if __name__ == '__main__':
#     unittest.main()