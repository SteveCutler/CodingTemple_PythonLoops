# Objective:
# Advance your looping skills by exploring more complex list manipulations. 
# You will learn to selectively loop through parts of a list, use list 
# comprehensions for concise code, and generate numerical lists with Python's range function.

# Task 1: The Selective DJ
# Loop through a slice of the genres list from the previous question 
# and print out the genres. Use slicing to create a sublist of genres 
# from the second to the fourth track.

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genres_sublist = genres[1:4]
i=0
while i <= len (genres_sublist)-1:
    print(genres_sublist[i])
    i+=1

print(genres_sublist)


# Task 2: The One-Liner Band with List Comprehensions
# Use a list comprehension to create a new list that contains each 
# genre with the word "Music" appended to it. Print this new list.

genresMusic = [x + " music" for x in genres]
print(genresMusic)



# Task 3: Numerical Beats with range
# Write a loop using range() to print out a countdown from 10 to 1, 
# followed by the message "The beat drops now!".
z = 10
while z in range (11):
    if z >0:
        print(z)
        z -=1
    else:
        print("The beat drops now!")
        break

