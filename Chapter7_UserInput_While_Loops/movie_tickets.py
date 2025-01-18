prompt = "\nHow old are you? "
prompt += "\nType 'quit' to exit the program."

prompt = input(prompt)

# print(prompt)

while True:
    if prompt == 'quit':
        break
    prompt = int(prompt)
    if prompt < 3:
        print("The ticket is free.")
    elif prompt <= 12:
        print("The ticket is $10.")
    elif prompt > 12:
        print("The ticket is $15")
    break
