shopping_list = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent" and command[1] not in shopping_list:
        shopping_list.insert(0, command[1])
    elif command[0] == "Unnecessary" and command[1] in shopping_list:
        shopping_list.remove(command[1])
    elif command[0] == "Correct" and command[1] in shopping_list:
        index_old = shopping_list.index(command[1])
        shopping_list[index_old] = command[2]
    elif command[0] == "Rearrange" and command[1] in shopping_list:
        index = shopping_list.index(command[1])
        shopping_list.append(shopping_list.pop(index))
    command = input()

print(", ".join(shopping_list))
