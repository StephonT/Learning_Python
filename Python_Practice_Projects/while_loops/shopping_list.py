shopping_list = []

while True:
    item = input("\nWhat would you like to add to your shopping list? Type 'done' when you are finished.")
    
    if item.lower() == 'done':
        break
    
    shopping_list.append(item)
    
    

print(f"\nFinal List: {shopping_list}")