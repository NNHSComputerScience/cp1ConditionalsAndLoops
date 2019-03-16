# boolean values and logical operators
import random

# 2 BOOLEAN VALUES: 
#   in shell...
'''
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type("False")
	 
<class 'str'>
>>> 
'''

# a BOOLEAN EXPRESSION 
#  in shell...
'''
>>> 5 == 5
	 
True
>>> 5 != 5
	 
False
>>> 5 < 10
	 
True
>>> 5 >= 10
	 
False
>>> 
'''

# LOGICAL OPERATORS: and, or, not
#   order of precendence is: not, and, or
#   https://runestone.academy/runestone/static/thinkcspy/Selection/PrecedenceofOperators.html

# CHALLENGE: Generate a random number between 1 and 13 and
#            print "Your number is lucky." if the number is 7, 11, or 13.
lucky_num = random.randint(1,13)
print(lucky_num)
# the following condition will always evaluate to True
#   refer to the below example
#if lucky_num == 7 or 11 or 13:
if lucky_num == 7 or lucky_num == 11 or lucky_num == 13:
    print("Your number is lucky.")

if 1:
    if "Hi":
        if 5.5:
            print("All evaluated to True")

if 0 or 0.0 or "":
    print("One evaluated to True")
else:
    print("All evaluated to False")


def calcLetterGrade(percentage):
    if(percentage >= 90):
        letter_grade = "A"
    # this overchecks the value of percentage
    #   We know that percentage must be < 90 if the
    #       elif is executed.
    #elif(percentage >= 80 and percentage < 90):
    elif(percentage >= 80):
        letter_grade = "B"
    elif(percentage >= 70):
        letter_grade = "C"
    elif(percentage >= 60):
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    print("The grade is " + letter_grade)

# call our new function
calcLetterGrade(85)
calcLetterGrade(91)

# CHALLENGE: Exclusive Network
'''
With a partner, write a Python program to grant access to an exclusive computer network.
- Get a username and password from the user
- Check to see if the username/password matches any of the exclusive member username/passwords
- Allow guest access if ‘guest’ is the username OR the password
- Print a message including the username if they gained access
- Print message denying access if the login credentials are incorrect

Extension challenges:
- Can you loop the program to allow the user to try entering the password again if they fail?
- Can you make the program only give them 3 opportunities to re-enter their password?
- Can you make the program check their password to be sure it's secure? (check for at least
    8 characters, at least one numeric, and at least one special character (!, $, &) )
- What other features would an exclusive network have?

'''


input("Press enter to exit.")
