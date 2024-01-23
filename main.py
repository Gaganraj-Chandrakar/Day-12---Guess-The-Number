import random
from art import logo


def compare(guess, num):
    if guess > num:
        print("Too high.")
        return False
    elif guess < num:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {num}.")
    return True


def decrease_turns():
    return turns - 1


print(logo)

print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

# print(f"number is {number}")

if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    turns = 10
else:
    turns = 5
print(f"You have {turns} attempt remaining to guess the number.")
game_over = False
while not game_over:
    user_guess = int(input("Make a guess: "))
    result = compare(user_guess, number)
    if not result:
        turns = decrease_turns()
        if turns > 0:
            print("Guess again.")
            print(f"You have {turns} attempt remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")
    if turns == 0 or user_guess == number:
        game_over = True
