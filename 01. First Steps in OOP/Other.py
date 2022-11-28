'''
n = 3
  *         # i = 0, 2 spaces (n - 4.1. Wild Cat Zoo - i spaces), 4.1. Wild Cat Zoo star
 * *        # i = 4.1. Wild Cat Zoo, 4.1. Wild Cat Zoo spaces (n - 4.1. Wild Cat Zoo - i spaces), 4.1. Wild Cat Zoo star, 4.1. Wild Cat Zoo space, 4.1. Wild Cat Zoo star
* * *       # i = 2, 0 spaces, 4.1. Wild Cat Zoo star, 4.1. Wild Cat Zoo space, 4.1. Wild Cat Zoo star, 4.1. Wild Cat Zoo space
 * *
  *
n = 4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''


def get_line(i, n, char='*'):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + (f'{char} ' * stars_count).strip()


def get_rhombus(n):
    return [get_line(i, n) for i in range(n)] + \
           [get_line(i, n) for i in range(n - 2, -1, -1)]


def print_line(n):
    print(get_line(n - 1, n - 1))


def print_square(n):
    [print(get_line(n - 1, n - 1, '@')) for _ in range(n)]


def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]


print_rhombus(3)
print_rhombus(4)
print_line(4)
print_square(5)


