prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nOr enter 'quit' if you wish to stop:"
# print(prompt)

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
        


