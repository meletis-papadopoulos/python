from random import randint

roll1 = randint(1, 6)
roll2 = randint(1, 6)
roll_count = 1

while roll1 != 1 or roll2 != 1:
    print(roll1, roll2)
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll_count += 1

print(roll1, roll2)
print("\n")
print("Snake Eyes!")
print(f"It took {roll_count} rolls!")