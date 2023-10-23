"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
from decimal import ROUND_DOWN
import random, statistics as st

# Create a list of successful attempts to get best record

records = {"Easy": [0], "Medium": [0], "Hard": [0]}


# Create the start_game function.
def start_game(records):

    # Welcome the players to the game
    print("\nWelcome to the Number Guessing Game\n")
    print("Can you beat the best records?")

    print("Easy: " + str(min(records["Easy"])) + "  Medium: " + str(min(records["Medium"])) +  "  Hard: " + str(min(records["Hard"])))  

    # Allow the player to select the difficulty
    difficulty = input("Would you like to play '(e)asy','(m)edium','(h)ard'?  ")

    # Create the bounds of the game based on choosen difficulty
    if difficulty.lower() == "e":
        magic_number = random.randint(1,10)
        outer_limit = 10

    elif difficulty.lower() == "m":
        magic_number = random.randint(1,100)
        outer_limit = 100

    else:
        magic_number = random.randint(1,1000)
        outer_limit = 1000

    # Start the Game!
    print(f"\nDifficulty Selected: {difficulty}")
    print(f"Im thinking of a number between 1 and {outer_limit}\n")
    
    # Set the number_of_guesses and lower_limit to 1 by default
    number_of_guesses = 1
    lower_limit = 1

    # Main Game loop
    # Update number of Guesses and store in records
    while True:
        guess = int(input("Pick a number  "))

        if guess > magic_number:
            outer_limit = guess
            print(f"Too High! [{lower_limit} - {outer_limit}]")
            number_of_guesses +=1

        elif guess < magic_number:
            lower_limit = guess
            print(f"Too Low!  [{lower_limit} - {outer_limit}]")
            number_of_guesses +=1
        else:
            print("Yes that is the number I was thinking of!\n")
            print(f"It took you {number_of_guesses} tries.\n")
            if difficulty == "e":
                records["Easy"].append(number_of_guesses)
            elif difficulty == "m":
                records["Medium"].append(number_of_guesses)
            else:
                records["Hard"].append(number_of_guesses)

            break

    # Call play_again function to ask player if they want to play again
    print(records)
    print_stats(records)
    play_again()

def play_again():
    again = input("Would you like to play again? [y/n]\n")
    if again.lower() == "y":
        start_game(records)
    else:
        print("Thank you for playing the game!  See you next Time!")

def print_stats(records):
    for k in records:
        if records[k] == []:
            records[k] = [0]
    print(records)
    stats = {"Easy": {"Mean": st.mean(records["Easy"]), "Median": st.median(records["Easy"]), "Mode": st.mode(records["Easy"])},
        "Medium": {"Mean": st.mean(records["Medium"]), "Median": st.median(records["Medium"]), "Mode": st.mode(records["Medium"])},
        "Hard": {"Mean": st.mean(records["Hard"]), "Median": st.median(records["Hard"]), "Mode": st.mode(records["Hard"])}}

    print("     *** GAME STATISTICS ***")
    print("------ Easy -- Medium -- Hard -----")
    print("Mean:   " + str(round(stats["Easy"]["Mean"])) + "        " + str(round(stats["Medium"]["Mean"])) + "        " + str(round(stats["Hard"]["Mean"])))
    print("Median: " + str(round(stats["Easy"]["Median"])) + "        " + str(round(stats["Medium"]["Median"])) + "        " + str(round(stats["Hard"]["Median"])))
    print("Mode:   " + str(round(stats["Easy"]["Mode"])) + "        " + str(round(stats["Medium"]["Mode"])) + "        " + str(round(stats["Hard"]["Mode"])))


start_game(records)








# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
