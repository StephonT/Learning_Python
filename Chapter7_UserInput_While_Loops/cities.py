prompt = "\nTell me which city you would like to visit:"
prompt += "\nOr enter 'quit' to end the program: "
# print(prompt)

message = ""

#You can simply use break to end a while loop rather than using a flag and having it equal to False to stop the while loop.
#A while loop that starts with 'while True' will run forever unless break is used in the while loop
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to visit {city.title()}.")
