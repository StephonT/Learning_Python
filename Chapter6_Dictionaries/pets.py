# Dictionary in a list
pet_0 = {'type': 'cat', 'owner': 'Londyn'}
pet_1 = {'type': 'dog', 'owner': 'Leah'}
pet_2 = {'type': 'rabbit', 'owner': 'Qualicia'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['owner']} has a pet {pet['type']}.")
