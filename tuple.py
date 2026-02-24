cities = ("Chennai", "Delhi", "Mumbai", "Kolkata", "Coimbatore")

print("All Cities:")
for city in cities:
    print(city)

print("\nCities in Uppercase:")
for city in cities:
    print(city.upper())

print("\nCities with length greater than 6:")
for city in cities:
    if len(city) > 6:
        print(city)

count = 0
for city in cities:
    if city.lower().startswith('c'):
        count += 1

print("\nNumber of cities starting with 'C':", count)
