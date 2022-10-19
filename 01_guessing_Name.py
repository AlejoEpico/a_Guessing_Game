import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Plese type a number bigger than 0")
        quit()
else:
    print("please type a number")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a number")
        continue

    if user_guess == random_number:
        print("You got it")
        break

    else:
        if user_guess > top_of_range:
            print("You are above the number")
        else:
            user_guess < top_of_range
            print("You are under the number")

print("You got it in", guesses, "guesses")
