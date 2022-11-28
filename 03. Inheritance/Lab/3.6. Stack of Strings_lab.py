class Stack:
    def __init__(self):
        self.data = []

    def validate_if_string(self, value):
        if not isinstance(value, str):
            raise TypeError('Only strings can be appended to StringStack')

    def push(self, value):
        self.validate_if_string(value)
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        sorted_data = sorted(self.data, reverse=True)
        return f'[{", ".join(sorted_data)}]'


# string = Stack()
# # print(string.push(10))
# print(string.push("Ani"))
# print(string.top())
# print(string.is_empty())
# print(string.pop())
# print(string.is_empty())

stack = Stack()
stack.push("apple")
stack.push("carrot")

print(str(stack))
print(stack.pop())
print(stack.top())
stack.push("cucumber")
print(str(stack))
print(stack.is_empty())
