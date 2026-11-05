students = ["Ali","Maryam","Fatima","Rohan","Ramesh"]
print(students[0])
print(students[-1])

students[3] = "Donald"
students.append("Kumar")
students.insert(1, "Usman")
students.insert(1, "Mohammed")
students.remove("Ramesh")
students.pop(1)
print(students)
print("No of students =>", len(students))