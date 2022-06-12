numbers = list(map(int, input().split()))
command = input()
count = 0
while command != "End":
    target_index = int(command)
    value = 0
    if 0 <= target_index < len(numbers):
        value = numbers[target_index]
        for i in range(len(numbers)):
            if i == target_index:
                numbers[target_index] = -1
                count += 1
            if numbers[i] > value:
                numbers[i] -= value
            elif numbers[i] <= value and numbers[i] != -1:
                numbers[i] += value

    command = input()
print(f"Shot targets: {count} ->", end=" ")
print(*numbers, sep=" ")
