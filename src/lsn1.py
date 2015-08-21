__author__ = 'xkazuhira'

import random
import sys
import os

########################################################################################################################
## PART ONE: START

print("Hello world")  # Print with "()"

name = "KAZUHIRA"  # String variable
print(name)

# TYPES:
# Numbers Strings Lists Tuples Dictionaries

print("", (4+2)*2+4)  # Arithmetic
print("", 45//2)

quote = "\"I think therefore I am.\""  # special chars

multi_line_quote = ''' just
like everyone else '''  # Multi-line text

print("%s %s %s" % ('I like this', quote, multi_line_quote))  # %s insertion/formatting String

print("I don't like ", end="")  # no '\n' at the end-of-line
print("newlines")

print('\n'*5)  # Printing 5 newlines

## PART ONE: END
########################################################################################################################
## PART TWO: START

grocery_list = ["Juice", "Tomatoes", "Potatoes", "Bananas"]  # list

print("First Item", grocery_list[0])  # calling 1st element

grocery_list[0] = "Green Juice"  # Changing value on the list

print("First Item", grocery_list[0])  # check

print(grocery_list[1:3])  # Include from 1 to 3 - excluding 3

other_events = ["Wash Car", "Pick Up Kids", "Cash Check"]

to_do_list = [other_events, grocery_list]  # inserting list creating multi-dimensional array

print(to_do_list)  # Whole list
print(to_do_list[1][2])  # Should return potatoes

grocery_list.append("Onions")

print(to_do_list)

grocery_list.insert(1, "Pickle")  # Insert Pickle at position [1]

print(grocery_list)  # check

grocery_list.remove("Pickle")  # Remove pickle from array

grocery_list.sort()  # Sort in alphabetic order
grocery_list.reverse()  # Reverse array

print(grocery_list)  # check

to_do_list2 = other_events + grocery_list

print(to_do_list2)
print(len(to_do_list2))  # Length
print(max(to_do_list2))  # Last element
print(min(to_do_list2))  # First element

print('\n'*5)  # Printing 5 newlines

## PART TWO: END
########################################################################################################################
## PART THREE: START

pi_tuple = (3,1,4,1,5,9)  # 3.14159
# Can't be changed

new_tuple = list(pi_tuple)  # tuple -> list
new_list = tuple(pi_tuple)  # list -> tuple

print('\n'*5)  # Printing 5 newlines

## PART THREE: END
########################################################################################################################
## PART FOUR: START

something_something = {"Ur": "Balls?",
                       "My": "Peanut butter",
                       "Their": "Jelly",
                       "Us": "China"}

print(something_something['My'])

del something_something['Ur']

something_something['Their'] = "Something"

print(len(something_something))

print(something_something.get("Us"))

print(something_something.keys())  # Referring to all keys
print(something_something.values())  # Referring to all values

print('\n'*5)  # Printing 5 newlines

## PART FOUR: END
########################################################################################################################
## PART FIVE: START

age = 21

if age > 16:
    print("You're allowed in")
else:
    print("You're to young")

if age >= 21:
    print("Okay")
elif age < 21 and age >= 16:
    print("Less okay")
else:
    print("wtf are doing you young mate?")

if ((age >=1) and (age <= 18)):
    print("You get a birthday")
elif (age == 21) or (age >=65):
    print("Here, have a birthday")
elif not(age==30):
    print("You don't get a birthday")
else:
    print("You get a birthday party yeah")

## PART FIVE: END
########################################################################################################################
## PART SIX: START

for x in range(0, 10):
    print(x, ' ', end="")

print ('\n')

for y in grocery_list:
    print(y)

print ('\n')

for x in [2,4,6,8,10]:
    print(x)

print ('\n')

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

print ('\n'*5)

## PART SIX: END
########################################################################################################################
## PART SEVEN: START

random_num = random.randrange(0, 100)

while random_num != 15:
    print(random_num)
    random_num = random.randrange(0, 100)

print('\n' * 5)
i = 0

while i <= 20:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        break
    else:
        i += 1  # i = i + 1
        continue

    i += 1