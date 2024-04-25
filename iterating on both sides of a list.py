# Create two lists
names = ["John", "Mary", "Bob"]
ages = [30, 25, 40]

# Iterate over both lists using zip()
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
