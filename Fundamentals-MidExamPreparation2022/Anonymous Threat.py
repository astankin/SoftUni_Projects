def merge_func(string_list, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(string_list):
        end_index = len(string_list) - 1
    string_list[start_index:end_index + 1] = ["".join(string_list[start_index:end_index + 1])]


def divide_func(string_list, index, partitions):
    divider = len(string_list[index]) // partitions
    element = string_list[index]
    divided_elem = []
    for i in range(len(string_list[index]), divider):
        part = element[i:i + divider]
        if i < partitions * divider:
            divided_elem.append(part)
        else:
            divided_elem[-1] += part
    string_list[index:index + 1] = divided_elem


text_input = input().split()
data = input()
while data != "3:1":
    command, num1, num2 = data.split()
    num1 = int(num1)
    num2 = int(num2)
    if command == "merge":
        merge_func(text_input, num1, num2)
    elif command == "divide":
        divide_func(text_input, num1, num2)
    data = input()

print(" ".join(text_input))
