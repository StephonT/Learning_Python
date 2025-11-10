favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'rust', 'phil': 'python', "airika":"rust"}

participants = ['stephon', 'jahhad', 'jen',
                'edward', 'sarah', 'airika', 'phil']

# Looping through the list of participants to see who took the poll.
# for participant in participants:
#     if participant not in favorite_languages.keys():
#         print(f"\n{participant.title()}, you should take our poll!")
#     else:
#         print(f"\n{participant.title()}, thank you for taking our poll.")

for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")
    language = favorite_languages[name]
    print(f"I see you like {language}.")
    
for participant in participants:
    print(f"Hello, {participant.title()}")
    if participant not in name:
        print(f"{participant}, you should take our poll!")
    elif participant in name:
        language = favorite_languages[name]
        print(f"{participant.title()}, thank you for taking our poll. We see that your favorite language is {language}.")

# The set() prevents duplication
print("\nThe following languages were mentioned:")
for name in set(favorite_languages.values()):
    print(name.title())
    