n1 = int(input())
n2 = int(input())
higher = max(n1, n2)
value = higher
while True:
    if higher % n1 == 0 and higher % n2 == 0:
        print("НОК на", n1, "и", n2, "е", higher)
        break
    else:
        higher = higher + value
