import simplegui
import random
import math

# Global variables
secret_number = 0
num_range = 100
remaining_guesses = 7

def new_game():
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, num_range)
    remaining_guesses = math.ceil(math.log(num_range + 1, 2))
    print("\nNew game! Guess a number in range [0, " + str(num_range) + ")")
    print("You have " + str(remaining_guesses) + " guesses remaining.")

def input_guess(guess):
    global remaining_guesses
    guess = int(guess)
    remaining_guesses -= 1
    print("\nGuess was " + str(guess))
    
    if guess == secret_number:
        print("Correct! You win!")
        new_game()
    elif remaining_guesses == 0:
        print("Out of guesses! The secret number was " + str(secret_number) + ".")
        new_game()
    elif guess < secret_number:
        print("Higher")
        print("Guesses remaining: " + str(remaining_guesses))
    else:
        print("Lower")
        print("Guesses remaining: " + str(remaining_guesses))

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

# Create the frame
frame = simplegui.create_frame("Guess the Number", 200, 200)
frame.add_input("Enter your guess:", input_guess, 100)
frame.add_button("Range is [0,100)", range_100, 200)
frame.add_button("Range is [0,1000)", range_1000, 200)

# Start the game
new_game()
frame.start()
