# Objective:
# The aim of this assignment is to deepen your understanding of Python's 
# range() function and its application in loops. You will correct a 
# code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Your Mood Today
# Write a program that prints off different moods for 
# each day of the week. Create a list of moods such as 
# "Happy", "Sad", "Energetic", and "Calm". Using the 
# range() function, loop through the days of the week 
# and for each day, randomly select a mood from the list 
# and print it. Ensure that your program includes the 
# use of the random module to select the mood.

import random
weekdays = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
moods = ["happy","sad","energetic","calm","surprised","depressed"]

i = 0
while i in range(7):
    num = random.randint(0,5)
    print("On", weekdays[i],"you felt",moods[num])
    i += 1
    

# Example Outcome: An example output could be "On 
# Wednesday, you were feeling happy." "On Thursday 
# you were feeling sad." 