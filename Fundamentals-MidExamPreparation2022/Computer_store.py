price_without_taxes = 0
total_price = 0
sum_taxes = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break
    part_price = float(command)
    if part_price < 0:
        print("Invalid price!")
        continue
    price_without_taxes += part_price
    sum_taxes += part_price * 0.2
    total_price += part_price + (part_price * 0.2)

if total_price == 0:
    print("Invalid order!")
    exit()

if command == "special":
    total_price = total_price * 0.9

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {price_without_taxes:.2f}$")
print(f"Taxes: {sum_taxes:.2f}$")
print("-----------")
print(f"Total price: {total_price:.2f}$")