# Objective:
# The aim of this assignment is to explore the importance of the 
# loop condition in while loops. You will create loops with different 
# conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration
# Write a while loop with a condition that will never be true 
# (an infinite loop). Inside the loop, print a statement. 
# Then, use a break statement to exit the loop after 5 iterations.
x = 0
while x >= 0:
    print("loop is running",x)
    if x == 4:
        break
    else:
        x += 1

# Task 2: Conditional Exit
# Modify the infinite loop from Task 1 to include a condition 
# that will eventually be true and remove the break statement. 
# The loop should terminate naturally once the condition is met. 
        
x = 0
while x < 5:
    print("loop is running",x)
    x += 1