from _collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
success = True

print(max(orders))

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        success = False
        orders.appendleft(current_order)
        break

if success:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")


