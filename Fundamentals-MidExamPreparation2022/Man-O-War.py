pirate_ship_status = list(map(int, input().split(">")))
ware_ship_status = list(map(int, input().split(">")))
max_health_capacity = int(input())
data_input = input()
while data_input != "Retire":
    data_input = data_input.split()
    command = data_input[0]
    if command == "Fire":
        index = int(data_input[1])
        damage = int(data_input[2])
        if 0 <= index < len(ware_ship_status):
            ware_ship_status[index] -= damage
            if ware_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif command == "Defend":
        start_index = int(data_input[1])
        end_index = int(data_input[2])
        damage = int(data_input[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif command == "Repair":
        index = int(data_input[1])
        health = int(data_input[2])
        if 0 <= index < len(pirate_ship_status):
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_capacity:
                pirate_ship_status[index] = max_health_capacity
    elif command == "Status":
        count = [num for num in pirate_ship_status if num < max_health_capacity * 0.2]
        print(f"{len(count)} sections need repair.")

    data_input = input()
pirate_ship_sum = sum(pirate_ship_status)
ware_ship_sum = sum(ware_ship_status)
print(f"Pirate ship status: {pirate_ship_sum}")
print(f"Warship status: {ware_ship_sum}")