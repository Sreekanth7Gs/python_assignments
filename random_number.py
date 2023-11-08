import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100. Try to guess it.")
count = 0

while True:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess < 1 or guess > 100:
        print("Sorry, your guess is out of the valid range (1-100). Try again.")
    elif guess > secret_number:
        print("Your guess is too high. Try again.")
    elif guess < secret_number:
        print("Your guess is too low. Try again.")
    else:
        print(f"Great! You guessed the correct number in {count} attempts.")
        break

          