'''
List Trace 2
Pawelski
11/13/2023
Introduction to Computer Science
'''

classes = ["Math", "Science", "Social Studies", "English"]
classes.append("Computer Science")
classes.append("Tech Ed")
classes.insert(0, "Art")
classes.sort()

for i in range(0, len(classes)):
    print(classes[i])