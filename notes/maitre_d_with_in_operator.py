# Maitre D'
# Demonstrates treating a value as a condition & the in operator

# Values as conditions
#   for numbers, 0 evaluates to False, everything else to True
#   for strings, "" evaluates to False, everything else to True

# 'in' operator
#   Searches in a sequence(like a string) for a value and returns True if found

print ("Welcome to the Chateau D' Food")
print ("\nIt seems we are quite full this evening.")

name = input("\nWhat is the name?: ").title()
money = int(input("\nHow many dollars do you tip?: "))

# no comparison, but same as "if money != 0"; True if a tip is given
if money:   
    print ("Right this way to your table,", name + ".")
# searches for string in name; True if found
elif "Doctor" in name or "Dr." in name: 
    print ("Right this way to your table,", name + ". There's always room for \
a doctor at Chateau D' Food!")
else:
    print ("Please, wait.  It may be a while.")

input("\n\nPress the enter key to exit.")

