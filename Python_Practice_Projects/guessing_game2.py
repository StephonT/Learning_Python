guess_count = 0
guess_limit = 3
secret_number = 5


while guess_count < guess_limit:
    guess = int(input("Guess Secret Number: "))
    guess_count += 1
    if guess == secret_number:
        print("You guessed the correct number!")
        break
else:
    print("You've failed to guess the correct number.")
        