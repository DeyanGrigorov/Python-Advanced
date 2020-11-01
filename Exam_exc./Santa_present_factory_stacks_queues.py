# IT IS 50 % IN JUDGE
#  PROBLEM FROM STACKS AND QUEUES

from _collections import deque

materials = [int(n) for n in input().split()]
magic_values = deque([int(n) for n in input().split()])

presents = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}
presents_made = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}
product = 0
last_box = 0
magic_current = 0

while True:
    if len(materials) <= 0 or len(magic_values) <= 0:
        break
    for _ in range(len(materials)):
        last_box = materials.pop()
        for magic_current in magic_values:
            product = last_box * magic_current
            break
        break

    for present, magic in presents.items():
        if product == magic:
            materials.append(last_box)
            materials.pop()
            magic_values.popleft()
            presents_made[present] += 1
            break
        if product < 0:
            sum_the_two = last_box + magic_current
            materials.append(last_box)
            materials.pop()
            magic_values.popleft()
            materials.append(sum_the_two)
            break
        if magic_current == 0 and last_box == 0:
            magic_values.popleft()
            materials.append(last_box)
            materials.pop()
            break
        if magic_current == 0:
            magic_values.popleft()
            materials.append(last_box)
            break
        if last_box == 0:
            materials.append(last_box)
            materials.pop()
            break
    else:

        magic_values.popleft()
        materials.append(last_box)
        materials.pop()
        last_box += 15
        materials.append(last_box)

pair_dol_train = {
    'Doll': 0,
    'Wooden train': 0,
}
pair_bear_bicycle = {
    'Teddy bear': 0,
    'Bicycle': 0
}

for key, value in presents_made.items():
    if value > 0:
        if key == 'Doll':
            pair_dol_train[key] = value
        if key == 'Wooden train':
            pair_dol_train[key] = value
        if key == 'Teddy bear':
            pair_bear_bicycle[key] = value
        if key == 'Bicycle':
            pair_bear_bicycle[key] = value

first_pair = all(value > 0 for value in pair_bear_bicycle.values())
second_pair = all(value > 0 for value in pair_dol_train.values())

if first_pair or second_pair:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials) > 0:
    materials.reverse()
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if len(magic_values) > 0:
    magic_values.reverse()
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')


if first_pair:
    for k, v in sorted(pair_bear_bicycle.items()):
        print(f'{k}: {v}')
if second_pair:
    for k, v in sorted(pair_dol_train.items()):
        print(f'{k}: {v}')
if first_pair is False and second_pair is False:
    for key, value in presents_made.items():
        if value > 0:
            print(f"{key}: {value}")





