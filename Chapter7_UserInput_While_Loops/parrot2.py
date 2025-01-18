prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nOr enter 'quit' if you wish to stop:"

# Active is a 'flag'. The while loop will only check for one condition rather than many which could become very complicated
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
