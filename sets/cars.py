showroom = set()

showroom.add("Showroom Car 1")
showroom.add("Showroom Car 2")
showroom.add("Showroom Car 3")
showroom.add("Showroom Car 4")

print("Showroom Length")
print(len(showroom))
print()

showroom.add("Showroom Car 4")

print("Showroom with added car")
print(showroom)
print()

showroom.update({"Showroom Car 5", "Showroom Car 6"})

showroom.discard("Showroom Car 1")

print("Showroom with additional addition")
print("and 1 car discarded")
print(showroom)
print()

junkyard = set()

junkyard.add("Showroom Car 3")
junkyard.add("Showroom Car 4")
junkyard.add("Junkyard Car 1")
junkyard.add("Junkyard Car 2")
junkyard.add("Junkyard Car 3")
junkyard.add("Junkyard Car 4")

print("Junkyard")
print(junkyard)
print()

print("Showroom Junkard Intersection")
print(showroom.intersection(junkyard))
print()

print(showroom)
print()

print("Showroom Junkard Union")
print(showroom.union(junkyard))
