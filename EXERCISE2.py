numbers = []
while True:
    userNumber = input("Enter a number (or press Enter to quit):")

    if userNumber == "":
        break

    try:
        number = float(userNumber)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

    numbers.sort(reverse=True)
    fiveGreatestNumbers = numbers[:5]

    print(" The five greatest numbers in descending order are:",fiveGreatestNumbers)