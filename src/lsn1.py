__author__ = 'xkazuhira'

import random
import sys
import os

########################################################################################################################
## PART ONE: START

print("Hello world") # Print with "()"

name = "KAZUHIRA" # String variable
print(name)

# TYPES:
# Numbers Strings Lists Tuples Dictionaries

print("", (4+2)*2+4) # Arithmetic
print("", 45//2)

quote = "\"I think therefore I am.\"" # special chars

multi_line_quote = ''' just
like everyone else '''  # Multi-line text

print("%s %s %s" % ('I like this', quote, multi_line_quote)) # %s insertion/formatting String

print("I don't like ", end="") # no '\n' at the end-of-line
print("newlines")

print('\n'*5) # Printing 5 newlines

## PART ONE: END
########################################################################################################################
## PART TWO: START

grocery_list = ["Juice", "Tomatoes", "Potatoes", "Bananas"] # list

print("First Item", grocery_list[0]) # calling 1st element

grocery_list[0] = "Green Juice" # Changing value on the list

print("First Item", grocery_list[0]) # check

print(grocery_list[1:3]) # Include from 1 to 3 - excluding 3

other_events = ["Wash Car", "Pick Up Kids", "Cash Check"]

to_do_list = [other_events, grocery_list] # inserting list creating multi-dimensional array

print(to_do_list) # Whole list
print(to_do_list[1][2]) # Should return potatoes

grocery_list.append("Onions")

print(to_do_list)

grocery_list.insert(1, "Pickle") # Insert Pickle at position [1]

print(grocery_list) # check

grocery_list.remove("Pickle") # Remove pickle from array

grocery_list.sort() # Sort in alphabetic order
grocery_list.reverse() # Reverse array

print(grocery_list) # check