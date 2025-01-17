# Changing a string to an integer
seats = input("How many people are in your dinner group?")
seats = int(seats)

if seats > 8:
    print("You will have to wait for a table.")
else:
    print("You're table is ready.")
