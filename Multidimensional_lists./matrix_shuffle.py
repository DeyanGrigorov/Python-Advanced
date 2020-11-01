def print_matrix(matrix):
    for i in range(m):
        print(' '.join(matrix[i]))


def print_not_valid():
    print('Invalid input!')


def valid_input(matrix, commands):
    if command != 'swap':
        print_not_valid()
    elif len(args) != 4:
        print_not_valid()
    row_one, col_one, row_two, col_two = list((map(int, args)))

    if row_one < 0 or row_one >= m \
            or row_two < 0 or row_two >= m \
            or col_one < 0 or col_one >= n \
            or col_two < 0 or col_two >= n:
        print_not_valid()
    else:
        return True


m, n = [int(i) for i in input().split()]
matrix = [[r for r in input().split()] for row in range(m)]
rows = len(matrix)
cols = len(matrix[0])
total_length = rows * cols

command, *args = input().split()

while command != 'END':
    if valid_input(matrix, command):
        row_one, col_one, row_two, col_two = list(map(int, args))
        matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
        print_matrix(matrix)
    else:
        print_not_valid()

    command, *args = input().split()
