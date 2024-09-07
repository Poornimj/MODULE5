import math
number = int(input("Enter an integer to check if it's a prime number:"))
def isPrime(number):

    if number < 2:
        return False

    for i in range(2, int (math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

if isPrime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

