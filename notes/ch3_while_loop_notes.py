# while loop notes

# IN ENGLISH (PSEUDOCODE):
# if condition is True:
#   run some block of code
#   if false, block is skipped
# else:
#   this block runs if no other conditions are true

# while condition is True:
#   repeatedly run this block of code (body of the loop)
#   until condition becomes False
# loop is finished, program continues sequentially
   
# How to use a counter
#   Keeps track of number of times loop is executed.

print("Let's count to 100!")
# 2. What has to be initialized before the loop starts?
counter = 1

# 1. What is the condition that keeps the loop running?
while counter <= 100:
    # 3. What has to be done inside the loop?
    print("The count is at ", counter)
    counter += 1

# 4. What has to be done after the loop?
print("All done counting!")

# Common mistake: not updating the sentinel variable
#   (results in an infinite loop)

total = 0
num = int(input("Enter an integer (enter 0 to stop): "))
while(num != 0):
    total += num
    num = int(input("Enter an integer (enter 0 to stop): "))
print("Total: " + str(total))

#alternative
total = 0
num = 1 # set num to a value other than 0
while(num != 0):
    num = int(input("Enter an integer (enter 0 to stop): "))
    total += num
print("Total: " + str(total))

# Countdown Challenge (on own)
#   Make a counter that counts down from 10 and then says "BLAST OFF!"
count = 10
while count > 0:
    print(count)
    count -= 1
print("BLAST OFF!")


# Count by 5's Challenge(on own)
#   Count 0-100 by 5's
#   Print a message to tell the user when the count is half-way done

count = 0
countEnd = 100
print("\n\nLet's count to 100 by 5s!")
input("Press enter to start the counter")

while count <= countEnd:
    print("The count is at: ", count)
    if count == countEnd/2:
        print("Halfway there!")
    count += 5


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


# die_roller2 Challenge (partner)
#   Display how many evens after 5 rolls of a die.








