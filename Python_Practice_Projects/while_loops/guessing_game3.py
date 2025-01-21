secret_number = 4
guess = 0


while guess != secret_number:
    guess = int(input("Guess the secret number?"))
    if guess < secret_number:
        print("Guess higher!")
    elif guess > secret_number:
        print("Guess lower!")
    else:
        print("You guessed the correct number!")
        print("Thanks for playing!")
        break
