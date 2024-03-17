# Objective:
# Dive into the heart of Python loops with a musical twist. 
# Your task is to explore different ways of looping through 
# lists, each with its unique style and purpose. By the end of 
# this assignment, you will be able to control your loops like 
# a DJ controls the tracks, ensuring each element gets its time to shine.

# Task 1: The for Loop DJ Set
# Using the provided genres list, write a for loop 
# that prints out each genre with a custom message. 
# Extend this task by adding a counter that displays 
# the number of the track before the genre.

# # Our playlist of genres
# genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
x = 0
for x in range(4):
    if x == 0:
        print("track",x+1,"is a cool",genres[x],"song")
    elif x == 1:
        print("track",x+1,"is a hardcore",genres[x],"song")
    elif x == 2:
        print("track",x+1,"is a smooth",genres[x],"song")
    else:
        print("track",x+1,"is a contemplative",genres[x],"song")

# Task 2: The Remix Artist with while
# Convert the for loop from Task 1 into a while loop. 
# Ensure it performs the same function but also includes 
# a condition to stop the loop if a certain genre is played for instance Hip-hop.
        
x = 0
while x in range(4):
    if genres[x] == "Hip-hop":
        print("the genre is",genres[x],"-- record scratch!")
        break
    else:
        if x == 0:
            print("track",x+1,"is a cool",genres[x],"song")
            x += 1
        elif x == 1:
            print("track",x+1,"is a hardcore",genres[x],"song")
            x += 1
        elif x == 2:
            print("track",x+1,"is a smooth",genres[x],"song")
            x += 1
        else:
            print("track",x+1,"is a contemplative",genres[x],"song")
            x += 1

# Task 3: Light Show Technician Loop
# Using the range() function, loop through the genres 
# list by index. For each genre, print out the track number 
# and a message that the light show is ready. Modify the 
# loop to skip a genre if it's not suitable for the light show, for instance Classical genre.

x = 0
while x in range(4):
    if genres[x] == "Classical":
        continue
    else:
        if x == 0:
            print("track",x+1,"is playing. The light show is ready.")
            x += 1
        elif x == 1:
            print("track",x+1,"is playing. The light show is ready.")
            x += 1
        elif x == 2:
            print("track",x+1,"is playing. The light show is ready.")
            x += 1

