n = int(input())


matrix = []

for _ in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)


primary_sum = 0

for row in range(n):
    col = row
    primary_sum += matrix[row][col]


secondary_sum = 0

for row in range(n):
    col = n - 1 - row
    secondary_sum += matrix[row][col]

print(abs(primary_sum - secondary_sum))
