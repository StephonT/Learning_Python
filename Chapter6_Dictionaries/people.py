# Ceate a list of dictionaries
person_0 = {'first_name': 'Stephon',
            'last_name': 'Treadwell', 'age': '33', 'city': 'Newark'}
person_1 = {'first_name': 'Londyn', 'last_name': 'Treadwell',
            'age': '0.1', 'city': 'N. Brunswick'}
person_2 = {'first_name': 'Leah',
            'last_name': 'Treadwell', 'age': '5', 'city': 'Edison'}

people = [person_0, person_1, person_2]

#Print the keys and values in the dictionary that are stored in a list. 
for person in people:
    print(f"This person's name is {person['first_name']} {person['last_name']}. {
          person['first_name']} is {person['age']} years old and from {person['city']}, NJ.")
