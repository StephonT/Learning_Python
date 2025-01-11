# Making a list from 1 to one million and printing the min,max,and sum of the list
numbers = []
for value in range(1, 1_000_000):
    numbers.append(value)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
