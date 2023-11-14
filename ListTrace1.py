'''
List Trace 1
Pawelski
11/13/2023
Introduction to Computer Science
'''

games = []
games.append("Monopoly")
games.append("Sorry!")
games.append("Risk")
games.insert(0, "Trouble")
games.remove("Sorry!")
games.sort()
games.insert(2, "Clue")
games.pop(1)

print(games)