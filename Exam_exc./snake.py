# MATRIX TYPE PROBLEM, BEST SOLUTION 100%
def is_in_territory(row, col, size):
    return 0 <= row < size and 0 <= col < size


n = int(input())
matrix = []
snake_row = 0
snake_col = 0
food_quantity = 0
burrow_pos = []
next_row = 0
next_col = 0

for each in range(n):
    each_row = list(input())
    if 'S' in each_row:
        snake_row = each
        snake_col = each_row.index('S')
    if 'B' in each_row:
        burrow_pos.append((each, each_row.index('B')))
    matrix.append(each_row)

while True:
    command = input()

    if command == 'left':
        next_row, next_col = snake_row, snake_col - 1
    elif command == 'right':
        next_row, next_col = snake_row, snake_col + 1
    elif command == 'up':
        next_row, next_col = snake_row - 1, snake_col
    elif command == 'down':
        next_row, next_col = snake_row + 1, snake_col

    if not is_in_territory(next_row, next_col, n):
        matrix[snake_row][snake_col] = '.'
        print('Game over!')
        break
    else:
        matrix[snake_row][snake_col] = '.'
    if matrix[next_row][next_col] == '-':
        matrix[next_row][next_col] = 'S'
        snake_row, snake_col = next_row, next_col
    elif matrix[next_row][next_col] == '*':
        food_quantity += 1
        matrix[next_row][next_col] = 'S'
        if food_quantity == 10:
            print('You won! You fed the snake.')
            break
        snake_row, snake_col = next_row, next_col
    elif matrix[next_row][next_col] == 'B':
        matrix[next_row][next_col] = '.'
        burrow_pos.remove((next_row, next_col))
        next_row = burrow_pos[0][0]
        next_col = burrow_pos[0][1]
        matrix[next_row][next_col] = 'S'
        snake_row, snake_col = next_row, next_col

print(f'Food eaten: {food_quantity}')
[print(''.join(row)) for row in matrix]
