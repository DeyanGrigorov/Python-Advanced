from collections import deque

n, m = [int(n) for n in input().split(' ')]
snake = deque(list(input()))

for row in range(n):
    s = ''
    for col in range(m):
        piece = snake.popleft()
        s += piece
        snake.append(piece)
    if row % 2 == 0:
        print(s)
    else:
        print(s[::-1])
