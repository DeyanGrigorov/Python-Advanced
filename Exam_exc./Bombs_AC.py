# STACKS AND QUEUES
from _collections import deque
bomb_effects = [int(i) for i in input().split(', ')]
bomb_casings = [int(i) for i in input().split(', ')]

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}
bombs_created = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0
}

to_end = False

while True:
    if to_end:
        break
    if len(bomb_effects) < 1 or len(bomb_casings) < 1:
        to_end = True
        print(f"You don't have enough materials to fill the bomb pouch.")
        break
    current_bomb = bomb_effects.pop(0)
    current_cassing = bomb_casings.pop()
    res = current_bomb + current_cassing
    if res not in bombs.values():
        bomb_effects.insert(0, current_bomb)
        bomb_casings.append(current_cassing - 5)
    else:
        for bomb, value in bombs.items():
            if value == res:
                bombs_created[bomb] += 1
                all_in = all(value > 2 for value in bombs_created.values())
                if all_in:
                    to_end = True
                    print(f'Bene! You have successfully filled the bomb pouch!')
                    break
                break

if not bomb_effects:
    print(f'Bomb Effects: empty')
else:
    bomb_effects = [str(i) for i in bomb_effects]
    print(f"Bomb Effects: {', '.join(bomb_effects)}")
if not bomb_casings:
    print(f'Bomb Casings: empty')
else:
    bomb_casings = [str(i) for i in bomb_casings]
    print(f"Bomb Casings: {', '.join(bomb_casings)}")
for key, value in sorted(bombs_created.items()):
    print(f"{key}: {value}")