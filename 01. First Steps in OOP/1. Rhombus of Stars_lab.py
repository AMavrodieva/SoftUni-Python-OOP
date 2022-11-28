def get_line(n, i, char="*"):
    count_spaces = n - 1 - i
    count_stars = i + 1
    return " " * count_spaces + f'{char} ' * count_stars


def get_rhombus(n):
    return [get_line(n, i) for i in range(n)] + \
        [get_line(n, i) for i in range(n-2, -1, -1)]


def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]


n = int(input())

print_rhombus(n)
