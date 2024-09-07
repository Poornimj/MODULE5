cities = []

for i in range(5):
    city = input(f"Enter the city name {i + 1}:")
    cities.append(city)

print(" The cities you entered as below: ")
for city in cities:
    print(city)
