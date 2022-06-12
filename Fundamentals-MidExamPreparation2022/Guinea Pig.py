food_kg = float(input()) * 1000
hey_kg = float(input()) * 1000
cover_kg = float(input()) * 1000
guinea_weight = float(input()) * 1000
for day in range(1, 31):
    food_kg -= 300
    if day % 2 == 0:
        hey_kg -= food_kg * 0.05
    if day % 3 == 0:
        cover_kg -= guinea_weight / 3
    if food_kg <= 0 or hey_kg <= 0 or cover_kg <= 0:
        print(f"Merry must go to the pet store!")
        break
if food_kg > 0 and hey_kg > 0 and cover_kg > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_kg / 1000:.2f}, Hay: {hey_kg / 1000:.2f}, Cover: {cover_kg / 1000:.2f}.")
