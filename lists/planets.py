planet_list = ["Mercury", "Mars"]
print(planet_list)
print()

planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)
print()

planet_list.extend(["Uranus", "Neptune"])
print(planet_list)
print()

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
print(planet_list)
print()

planet_list.append("Pluto")
print(planet_list)
print()

print(planet_list[0:4])
print()

del planet_list[8]
print(planet_list)
print()

spacecraft_list = []

spacecraft_list.append(("Pioneer 10", "Jupiter"))
spacecraft_list.append(("Pioneer 11", "Jupiter", "Saturn"))
spacecraft_list.append(("Voyager 1", "Jupiter", "Saturn"))
spacecraft_list.append(("Voyager 2", "Jupiter", "Saturn", "Uranus", "Neptune"))
spacecraft_list.append(("New Horizon", "Jupiter", "Pluto"))

print(spacecraft_list)
print()

for x in planet_list:
    print(x)
    for y in spacecraft_list:
        if x in y:
            print (y[0])
    print()
    