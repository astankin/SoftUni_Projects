energy = int(input())
distance = input()
count = 0
while distance != "End of battle":
    distance = int(distance)
    if energy >= distance:
        energy -= distance
        count += 1
        if count % 3 == 0:
            energy += count
    else:
        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        exit()
    distance = input()
print(f"Won battles: {count}. Energy left: {energy}")
