heroes = {name: {} for name in input().split(', ')}

while True:
    tokens = input().split("-")
    name = tokens[0]

    if name == 'End':
        break

    item = tokens[1]
    cost = int(tokens[2])

    if item not in heroes[name]:
        heroes[name][item] = cost

[print(f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}") for name in heroes]
