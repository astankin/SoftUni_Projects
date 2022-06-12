emp1_efficiency = int(input())
emp2_efficiency = int(input())
emp3_efficiency = int(input())
students_count = int(input())
time = 0
while students_count > 0:
    if time % 4 != 0:
        students_count -= emp1_efficiency + emp2_efficiency + emp3_efficiency
        if students_count <= 0:
            break
    time += 1

print(f"Time needed: {time}h.")
