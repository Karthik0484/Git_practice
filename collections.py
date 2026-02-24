names = []

for i in range(5):
    name = input("Enter name: ").strip()
    names.append(name)

print("\nAll Names:")
for name in names:
    print(name)

print("\nNames in Uppercase:")
for name in names:
    print(name.upper())

print("\nNames with length greater than 5:")
for name in names:
    if len(name) > 5:
        print(name)

count = 0
for name in names:
    if name.lower().startswith('a'):
        count += 1

print("\nNumber of names starting with 'A':", count)
