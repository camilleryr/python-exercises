my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}

for relative in my_family.keys():
    print(f"{my_family[relative]['name']} is my {relative} and is {my_family[relative]['age']} years old")