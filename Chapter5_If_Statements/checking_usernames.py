current_users = ["stephon", "jahhad", "airika", "abriel"]

new_users = ["Stephon", "Airika", "Monique", "Lebron", "Carl"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user} is unavailable.")
    else:
        print(f"{new_user} is available.")
