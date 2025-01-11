usernames = []

# This if statement checks if the list is empty or not. If the list is empty, the result will be true and it'll run the else statement.
if usernames:
    for user in usernames:
        print(f"Hello {user}!")
else:
    print("We need to find some users!")