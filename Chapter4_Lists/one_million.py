# Print number from 1 to 1 million
# for value in range(1,100_000_001):
# print(value)

squares = []

for value in range(1, 11):
    squares.append(value**2)

print(squares)

# List comprehension for the above for loop. Putting it into one line
squares = [value**2 for value in range(1, 11)]
print(f'List Comprehension: {squares}')
