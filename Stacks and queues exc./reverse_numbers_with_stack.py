def reverse(stack):

    new_stack = []

    for num in range(len(stack)):
        new_stack.append(stack.pop())

    return new_stack


n = input().split(' ')
items = n

while n:
    print(' '.join(reverse(items)))




