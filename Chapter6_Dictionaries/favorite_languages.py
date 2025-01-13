favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'rust', 'phil': 'python'}

participants = ['stephon', 'jahhad', 'jen',
                'edward', 'sarah', 'airika', 'phil']

# Looping through the list of participants to see who took the poll.
for participant in participants:
    if participant not in favorite_languages.keys():
        print(f"\n{participant.title()}, you should take our poll!")
    else:
        print(f"\n{participant.title()}, thank you for taking our poll.")
