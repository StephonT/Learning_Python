# Storing my friends favorite numbers in a dictionary
favorite_numbers = {
    'jahhad': 23,
    'airika': 15,
    'clayton': 6,
    'marvin': 300_000
}

print(f'Marvin\'s favorite number is {favorite_numbers['marvin']}.')
print(f'Jahhad\'s favorite number is {favorite_numbers['jahhad']}.')
print(f'Clayton\'s favorite number is {favorite_numbers['clayton']}.')
print(f'Airika\'s favorite number is {favorite_numbers['airika']}.')

age = favorite_numbers.get('points', 'The point value does not exist.')
print(age)
