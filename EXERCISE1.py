import random

numOfRolls = int(input("Enter the number of rolls:"))
sum: int = 0
for i in range(numOfRolls):
    randomNumber = random.randint(1, 6)
    sum = sum + randomNumber

print(f" Sum of the numbers: {sum}")

