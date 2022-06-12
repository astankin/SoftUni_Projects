neighborhood = list(map(int, input().split("@")))
command = input()
curr_position = 0
while not command == "Love!":
    length = int(command.split()[1])
    curr_position += length
    if curr_position >= len(neighborhood):
        curr_position = 0
    if neighborhood[curr_position] > 0:
        neighborhood[curr_position] -= 2
    else:
        print(f"Place {curr_position} already had Valentine's day.")
        command = input()
        continue
    if neighborhood[curr_position] == 0:
        print(f"Place {curr_position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {curr_position}.")

if all(elem == 0 for elem in neighborhood):
    print("Mission was successful.")
else:
    missed_houses = [elem for elem in neighborhood if elem > 0]
    print(f"Cupid has failed {len(missed_houses)} places.")
