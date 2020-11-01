command = input()
numbers = list(map(int, input().split()))
summary = 0

if command == 'Odd':
    odd_list = []
    for number in numbers:
        if number % 2 != 0:
            odd_list.append(number)
    summary = sum(odd_list) * len(numbers)
elif command == 'Even':
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    summary = sum(even_list) * len(numbers)

print(summary)
