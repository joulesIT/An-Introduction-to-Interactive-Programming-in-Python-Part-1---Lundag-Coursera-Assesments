import random
import math

# Global variables
secret_number = 0
num_range = 100
remaining_guesses = 7

def new_game():
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, num_range)
    # Calculate number of guesses: smallest n such that 2**n >= high - low + 1
    remaining_guesses = math.ceil(math.log(num_range + 1, 2))
    print(f"\nNew game started! Guess a number in range [0, {num_range})")
    print(f"You have {remaining_guesses} guesses remaining.")

def input_guess(guess):
    global remaining_guesses
    guess = int(guess)
    remaining_guesses -= 1
    print(f"\nGuess was {guess}")
    print(f"Guesses remaining: {remaining_guesses}")

    if guess == secret_number:
        print("Correct! You win!")
        new_game()
    elif remaining_guesses == 0:
        print(f"Out of guesses! The secret number was {secret_number}.")
        new_game()
    elif guess < secret_number:
        print("Higher")
    else:
        print("Lower")

def range_100():
    global num_range
    num_range = 100
    print("Range set to [0, 100)")
    new_game()

def range_1000():
    global num_range
    num_range = 1000
    print("Range set to [0, 1000)")
    new_game()

# --- Simple console-based UI (no simplegui) ---
def main():
    new_game()
    print("\nCommands: enter a number to guess, 'r100' for range [0,100), 'r1000' for range [0,1000), 'q' to quit")
    while True:
        user_input = input("> ").strip()
        if user_input == 'q':
            break
        elif user_input == 'r100':
            range_100()
        elif user_input == 'r1000':
            range_1000()
        else:
            try:
                input_guess(user_input)
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()