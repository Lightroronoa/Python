import numpy as np

students = []
for i in range(11):
    name = input("fill records:")
    students.append(name)

students = np.array(students)
search_name = input("enter the name you want to search:")

found = False
for student in students:
    if student == search_name:
        print("got it")
        found = True
        break

if not found:
    print("not found")