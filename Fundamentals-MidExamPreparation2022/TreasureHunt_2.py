initial_loot = input().split("|")
data_input = input()

while data_input != "Yohoho!":
    removed_elements = []
    data_input = data_input.split()
    if data_input[0] == "Loot":
        for i in range(1, len(data_input)):
            if data_input[i] not in initial_loot:
                initial_loot.insert(0, data_input[i])
    elif data_input[0] == "Drop":
        index = int(data_input[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))
    elif data_input[0] == "Steal":
        count = int(data_input[1])
        if count >= len(initial_loot):
            print(", ".join(initial_loot))
            initial_loot = []
        else:
            num = len(initial_loot) - count
            removed_elements = initial_loot[num:]
            initial_loot = initial_loot[:num]
            print(", ".join(removed_elements))

    data_input = input()

if not initial_loot:
    print("Failed treasure hunt.")
else:
    sum_of_item_length = 0
    for elem in initial_loot:
        sum_of_item_length += len(elem)
    average_gain = sum_of_item_length / (len(initial_loot))
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")