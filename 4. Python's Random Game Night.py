# Objective:
# The aim of this assignment is to explore the random package 
# in Python and understand how it can be used with loops to 
# introduce randomness into your programs.

# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have 
# to guess which item in the list was selected. Use random.choice() 
# to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not.
import random
list = ["apple","bike","table"]
correct_choice = random.choice(list)
player_choice = input("Guess which item the computer selected: apple, bike or table")
print("player_choice =",player_choice," correct_choice =",correct_choice)

if correct_choice == player_choice:
    print("That's correct! the computer chose",player_choice)
else:
    print("Incorrect! Try again")