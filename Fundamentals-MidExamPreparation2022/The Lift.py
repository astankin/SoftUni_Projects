def is_lift_full(lift_state):
    for wagon in range(len(lift_state)):
        if lift_state[wagon] != 4:
            return False
    return True


number_of_people = int(input())
lift_state = list(map(int, input().split()))
for i in range(len(lift_state)):
    if lift_state[i] < 4 and number_of_people > 0:
        diff = 4 - lift_state[i]
        if number_of_people < diff:
            lift_state[i] += number_of_people
            number_of_people = 0
        else:
            number_of_people -= diff
            lift_state[i] += diff

if number_of_people == 0 and not is_lift_full(lift_state):
    print("The lift has empty spots!")
elif number_of_people > 0 and is_lift_full(lift_state):
    print(f"There isn't enough space! {number_of_people} people in a queue!")
print(' '.join(map(str, lift_state)))
