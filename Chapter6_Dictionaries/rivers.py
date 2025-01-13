rivers = {'Amazon River':'South America', 'Nile':'Egypt', 'Mississippi River':'Minnesota', 'Volga River':'Europe'}

#For loop to print key and value in a sentence
for key, value in rivers.items():
    print(f'\nThe {key} runs through {value}.')
    
#For loop to print keys in a dictionary only. You can also use .keys()
for river in rivers:
    print(f'\n{river}')
    
#For loop to print values in a dictionary only
for country in rivers.values():
    print(f'\n{country}')