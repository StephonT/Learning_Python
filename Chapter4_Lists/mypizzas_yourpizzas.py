fave_pizza = ['plain', 'extra cheese', 'beef']
# Setting the friend pizza list to be the same as my favorite list
friend_pizzas = fave_pizza[:]


fave_pizza.append('white slice')
friend_pizzas.append('bbq chicken')

print(f'My favorite pizzas are: ')
for pizza in fave_pizza:
    print(pizza)

print(f'\nMy friend\'s favorite pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)
