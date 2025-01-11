programming_words = {
    'slice': '\nTo extract certain information out of a list',
    'dictionary': '\nTo store information about an object',
    'if_statement': '\nA program that will run if a condition is true or false.'
}

print(programming_words['slice'])
print(programming_words['dictionary'])
print(programming_words['if_statement'])

# Looping through the dictionary using items which prints the key and value
for key, value in programming_words.items():
    print(f"\nKey: {key}")
    print(f"\Value: {value}")

# Looping through the dictionary using keys() which prints the key of a dictionary.
#The default behavior of looping through dictionaries is to print the keys only. So you dont have to use the keys() method if you dont want to.
for program in programming_words.keys():
    print(program)
