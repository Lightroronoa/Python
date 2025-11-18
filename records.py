import numpy as np

students = []
students_number = int(input("enter the number of total students:"))

for i in range(students_number):
    name = input("fill records:")
    students.append(name)

students = np.array(students)
search_name = input("enter the name you want to search:")

found = False
for student in students:
    if student == search_name:
        print("Found")
        found = True
        break

if not found:
    print("not found")