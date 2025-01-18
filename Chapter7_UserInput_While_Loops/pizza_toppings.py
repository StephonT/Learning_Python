prompt = "\nEnter in the topping you wish to put on your pizza:"
prompt += "\nWhen done, enter 'quit': "

# print(prompt)
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != 'quit':
        print(f"{topping.title()} will be added to your pizza.")
