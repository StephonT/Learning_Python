# Create a list of the multiples of three. Printing those numbers and adding them to a list
multiples_of_three = []

for value in range(3, 30, 3):
    multiples_of_three.append(value)
    print(value)

print(f'Multiples of three list: {multiples_of_three}')

# List comprehension practice
threes = [value for value in range(3, 30, 3)]
print(threes)
