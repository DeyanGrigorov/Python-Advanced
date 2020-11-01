n = int(input())

stack = []

for _ in range(n):

    tokens = input().split()

    command = int(tokens[0])

    if command == 1:
        stack.append(tokens[1])
    if stack:
        if command == 2:
            stack.pop()
        if command == 3:
            print(max(stack))
        if command == 4:
            print(min(stack))

print(', '.join([str(x) for x in reversed(stack)]))

