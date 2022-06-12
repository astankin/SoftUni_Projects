values = [int(num) for num in input().split()]
data = input()
while data != "end":
    if data == "decrease":
        values = list(map(lambda x: x-1, values))
    else:
        command, index1, index2 = data.split()
        index1 = int(index1)
        index2 = int(index2)
        if command == "swap":
            values[index1], values[index2] = values[index2], values[index1]
        elif command == "multiply":
            values[index1] = values[index1] * values[index2]

    data = input()
print(*values, sep= ", ")
