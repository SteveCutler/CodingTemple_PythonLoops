# Objective:
# The aim of this assignment is to practice using nested 
# loops in Python. You will correct a nested loop code 
# snippet, simulate a mood tracker, and generate a multiplication table.

# Task 1: Your Mood Tracker
# Simulate a mood tracker that records your mood at three 
# different times of the day (morning, afternoon, evening) for 
# each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner 
# loop should iterate over the times of the day. For each time, 
# randomly select a mood from a predefined list and print it.

# Example Outcome: An example would be "On Tuesday afternoon 
# you were sad" "On Tuesday night you were happy" "On Wednesday 
# morning you were tired"

import random
weekdays = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
moods = ["happy","sad","energetic","calm","surprised","depressed"]
timesOfDay = ["morning","afternoon","evening"]

i = 0
while i in range(0,7):
    x = 0
    for x in range(3):
        num = random.randint(0,5)
        print("On", weekdays[i],timesOfDay[x],"you were",moods[num])
    i += 1