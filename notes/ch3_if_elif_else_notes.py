# Ch. 3 Notes: Intro to modules; Intro to if-elif-else
#   How to use branching logic in Python.

# A) MODULES are files that contain code you can import to use in your own program.

# The random module contains functions related to generating pseudorandom numbers.
#   Import like this at the top of your program:
import random

# randint() function:
#   Req 2 int arguments & returns random # between those 2 values (inclusive).
num = random.randint(1, 10)
print(num)

# randrange() function:
#   Req 1 int argument & returns random # from 0 (inclusive) to the
#       specified value (exclusive)
num = random.randrange(10)  # from 0 to 9, including 0 and 9; starts at 0!
print(num)
num += 1                    # from 1 to 10, including 1 and 10
print(num)

# Challenge: Dice Challenge 1
#   Create 2 die variables.  Simulate rolling each die by generating a
#   random number between 1 and 6 and printing it. Can you use 2 diff methods?
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
print("Roll 1 = ", die1)
print("Roll 2 = ", die2)

# -------------------------------------------------------------
# B)if statement (binary bypass)
#   Block of code executes if condition is true. 
#       CONDITIONAL STATEMENT: A true/false statement that can be
#           evaluated and acted upon in one way if true and another if false

password = input("Please eneter your password: ");

if password == "nnhs":          # == is the equality (is equal to) operator
    print("access granted")


# Challenge: Simple if
#   Generate a random number, 1-99, and print "You generated a 2 digit number!"
#   if the random number generated is greater than 9.
num = random.randint(1, 99)
print(num)
if num > 9:
    print("You generated a number with more than one digit!")

# COMPARISON OPERATORS
#   ==      equality (is equal to)
#   !=      inequality (is not equal to)
#   >       greater than
#   <       less than
#   >=      greater than or equal to
#   <=      less than or equal to

# -------------------------------------------------------------
# C)if - else (binary choice)
#   if block executes if condition is true;
#   else block executes if condition is false.
password = input("Please enter your second password: ");
if password == "nnhs":
    print("access granted!")
else:
    print("access denied!")



# Challenge: Coin flip
#   Create a coin flipping simulator to randomly flip a coin to be heads/tails.
#   if heads, print "Heads"; if tails, print "Tails"

# -------------------------------------------------------------
# D)if - elif - else
#   if block executes if condition is true;
#   elif block executes if condition is true;
#   else block executes if condition is false.

password = input("Please enter your third password: ")

if password == "nnhs":
    print("access granted!")
elif password == "NNHS":
    print("access granted!")
elif password == "Nnhs":
    print("access granted!")
else:
    print("access denied!")


# Challenge: Ice Cream Challenge
#   Remember our ice cream algorithm? Recreate your own below, e.g.:
#   get flavor from user.
#   if user wants vanilla, "You get Vanilla"
#   elif user wants chocolate, "You get Chocolate"
#   elif user wants strawberry, "You get Strawberry"
#   else, "Sorry we don't have that flavor. Here's your Pistachio."

