initial_loot = input().split("|")
data_input = input()


def loot(loot_list, data):
    for i in range(1, len(data)):
        if data[i] not in loot_list:
            loot_list.insert(0, data[i])
    return loot_list


def drop(loot_list, index):
    if 0 <= index < len(loot_list):
        loot_list.append(loot_list.pop(index))


def steal(loot_list, count):
    if count >= len(loot_list):
        print(", ".join(loot_list))
        loot_list = []
    else:
        num = len(loot_list) - count
        removed_elem = loot_list[num:]
        loot_list = loot_list[:num]
        print(", ".join(removed_elem))
    return loot_list


while data_input != "Yohoho!":
    data_input = data_input.split()
    if data_input[0] == "Loot":
        loot(initial_loot, data_input)
    elif data_input[0] == "Drop":
        drop(initial_loot, int(data_input[1]))
    elif data_input[0] == "Steal":
        initial_loot = steal(initial_loot, int(data_input[1]))

    data_input = input()

if not initial_loot:
    print("Failed treasure hunt.")
else:
    sum_of_item_length = 0
    for elem in initial_loot:
        sum_of_item_length += len(elem)
    average_gain = sum_of_item_length / (len(initial_loot))
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
