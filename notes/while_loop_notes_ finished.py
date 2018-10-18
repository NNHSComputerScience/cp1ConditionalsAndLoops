# while loop notes

# IN ENGLISH (PSEUDOCODE):
# if condition is True:
#   run some block of code
#   if false, block is skipped
# else:
#   this block runs if no other conditions are met

# while condition is True:
#   continue to run this block of code (loop)
#   until condition becomes False
# loop finished, program continues sequentially

# WHILE LOOP: control structure that allows you to repeat blocks of code
#				based on a condition
# SENTINEL VALUE: the value that causes the loop to end (checked in the condition)
    
# How to use a counter
#   Keeps track of number of times loop is executed.
#	!!! annotate with #1, #2, #3, #4 to match questions
counter = 0
print ("Let's count to 100!")
input("Press enter to start the counter.")
while counter < 101:    # sentry variable = counter
    print ("The count is at: ", counter)
    counter += 1

# Common mistake: not updating sentry variable (results in infinite loop)

input("Press enter to exit.\n\n\n")

# Countdown Challenge (on own)
#   Make a counter that counts down from 10 and then says "BLAST OFF!"

print("Let's count down to BLAST OFF!")
input("Press enter to start the countdown.")
count = 10

while count > 0:
    print(count)
    count -= 1

print("BLAST OFF!")

input("\nPress enter to exit.")

# Count by 5's Challenge(on own)
#   Count 0-100 by 5's
#   Print a message to tell the user when the count is half-way done

count = 0
end = 100

print("\n\nLet's count to 100 by 5's!")
input("Press enter to start the counter.")
 
while count <= end:
    print("The count is at: ", count)
    if count == (end / 2):
        print("Half-way there!")
    count += 5

input("\nPress enter to exit.\n")

# die_roller Challenge (partner)
#   Guess how many rolls it takes to roll a 5?

import random

# initialize variables
guess = int(input("How many rolls to get a 5? "))
rolls = 0
die = 0

# loops if roll is not a 5
while die != 5:
    die = random.randint(1,6)
    print("you rolled a", die)
    rolls += 1      # counts number of rolls
    
print("It took", rolls, "rolls to roll a 5!")

# check if user's guess was correct
if guess == rolls:
    print("Congrats! You guess it right!")
else:
    print("I'm sorry, you guessed incorrectly.")

input("\nPress enter to exit.")

# die_roller2 Challenge (partner)
#   Display how many evens after 5 rolls of a die.

input("\nPress enter to exit.")





