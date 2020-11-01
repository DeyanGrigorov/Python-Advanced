def get_magic_triangle(rows):
    triangle = [[1] * i for i in range(1, rows + 1)]
    for row in range(2, rows):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    return triangle


get_magic_triangle(5)