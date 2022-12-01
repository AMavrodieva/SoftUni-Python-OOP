def reverse_text(string):
    text = string[::-1]
    index = 0
    while index < len(text):
        yield text[index]
        index += 1


for char in reverse_text("step"):
    print(char, end='')


#  Решение на лекцията
def reverse_text(text):
    index = 0
    n = len(text)
    while index < n:
        yield text[n - index - 1]
        index += 1


for char in reverse_text("step"):
    print(char, end='')