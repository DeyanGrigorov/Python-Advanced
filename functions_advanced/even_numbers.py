numbers = list(map(int, input().split()))
even_list = []

for number in numbers:
    if number % 2 == 0:
        even_list.append(number)
print(even_list)