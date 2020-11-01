box_with_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack = 0
needed_racks = 0
end = False

while len(box_with_clothes) > 0:

    for _ in box_with_clothes:
        current = box_with_clothes.pop()
        rack += current

        if rack > rack_capacity:
            box_with_clothes.append(current)
            needed_racks += 1
            rack = 0
        elif rack == rack_capacity:
            needed_racks += 1
            rack = 0

if len(box_with_clothes) <= 0:
    end = True
if end and rack > 0:
    needed_racks += 1
    rack = 0

print(needed_racks)
