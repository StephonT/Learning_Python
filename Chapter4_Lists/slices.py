# Slicing these lists
animals = ['dog', 'cat', 'hamster', 'bird', 'lion']

# Printing the first 3 items
print(f'The first three animals in the list are: {animals[0:3]}')

# Printing three items from the middle of the list
print(f'\nThe three animals in the middle of the list are: {animals[1:4]}')

# Last three items of a list
print(f'\nThe last three animals in the list are: {animals[2:5]}')

print('The first three animals are as follows:')
for animal in animals[:3]:
    
    print(animal)
