'''
String Trace
Pawelski
11/13/2023
Introduction to Computer Science
'''

first_name = "Bobby"
last_name = "Brown"
full_name = last_name + " " + first_name

for letter in full_name:
    if letter != " ":
        print(letter + ", ", end="")