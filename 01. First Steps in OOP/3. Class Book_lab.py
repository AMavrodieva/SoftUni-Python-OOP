class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{book.name}{book.author}{book.pages}'


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


# Второ решение
class Book1:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{book.name}\n{book.author}\n{book.pages}'


book = Book_1("My Book", "Me", 200)
print(book)
print(str(book))  # this calls `__str__`
