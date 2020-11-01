m, n = list(map(int, input().split(' ')))

matrix = [[''] * n for i in range(m)]

num_squares = 0

for i in range(m):
    row = input().split(' ')
    for j in range(n):
        matrix[i][j] = row[j]

        if i - 1 >= 0 and j - 1 >= 0:
            if matrix[i][j] == matrix[i][j - 1] and \
               matrix[i][j] == matrix[i - 1][j] and \
               matrix[i][j] == matrix[i - 1][j - 1]:
                num_squares += 1

print(num_squares)