# Tuples, which are immutable or can't be changed
buffet = ("mac and cheese", "rice", "chicken", "corn", "beef")


print("Original List:")
for food in buffet:
    print(food)

# Try to modify list. Throws an error
# buffet[0] = cabbage
# print(buffet)
print("\nUpdated list:")
buffet = ("cabbage", "rice", "beans", "chicken")
for food in buffet:
    print(food)
