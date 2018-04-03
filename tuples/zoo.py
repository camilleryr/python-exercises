zoo = ("Panda", "Maybelle", "Tardigrade")

print("Index of 'Panda'")
print(zoo.index("Panda"))
print()

print("Is there a 'Maybelle' in the list?")
print("Maybelle" in zoo)
print()

print("Is there a 'Ellie' in the list?")
print("Ellie" in zoo)
print()

(item1, item2, item3) = zoo
print("Break Tuple apart into variables")
print(item1)
print(item2)
print(item3)
print()

zoo_list = list(zoo)

zoo_list.extend(["Chupacabre", "Mantee", "Maticore"])

zoo = tuple(zoo_list)

print("Convert to a list - add 3 more dope animals - convert back to tuple")
print(zoo)