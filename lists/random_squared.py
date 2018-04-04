import random

random_numbers = [random.randint(0, 49) for x in range(20)]

print(random_numbers)
print()

random_squared = [x**2 for x in random_numbers ]

print(random_squared)