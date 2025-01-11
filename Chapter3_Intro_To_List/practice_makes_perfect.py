# This file will be to practice each list function with one list

motorcycles = ['honda', 'kawasaki', 'suzuki', 's1000']
print(f'Original List: {motorcycles}')

#Listing objects in a list
print(f'My first bike was a {motorcycles[0].title()}.')
print(f'My second bike was a {motorcycles[1].title()}. I didnt like it too much to be honest.')
print(f'I had three {motorcycles[2].title()} bikes after that. It\'s safe to say I found my favorite brand of motorcycles.')
print(f'I wish I had a {motorcycles[-1]}! With my size, I\'ll be so uncomfortable.')
print(motorcycles)

#Replace object in list
motorcycles[-1] = 'slingshot'
print(motorcycles)

#Adding to a list using append
motorcycles.append('cruiser')
print(motorcycles)

#Removing an object from a list
motorcycles.pop(0)
print(motorcycles)