places = ['japan', 'hawaii', 'jamaica', 'brazil', 'africa']
print(places)
# Using sorted() does not change the order of your list. Does it temporarily
print(f'\nSorted List: {sorted(places)}')
print(f'Original List: {places}')

# Using sorted() to print in reverse alphabetical order
print(f'\nReverse Alphabetical Order: {sorted(places, reverse=True)}')
print(f'Original List: {places}')

# Using reverse to permantly reverse list
places.reverse()
print(f'\nPerm. Reversed List: {places}')
print(f'Original List: {places}')

# Use sort() to change the order of the list again
places.sort()
print(f'\nList Using sort(): {places}')

# Reverse alphabetical order using sort()
places.sort(reverse=True)
print(f'Reverse Alphabetical Order: {places}')
print(f'Original List: {places}')
