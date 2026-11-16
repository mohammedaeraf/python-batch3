# Union, intersection, and difference are common set operations.
# They compare two groups of students without repeating any item.
py_students = {"Ali", "Usman", "Zahra", "Fatima"}
web_students = {"Rohan", "Sunil", "Fatima", "Zahra"}

# union() returns all unique students from both sets.
print(py_students.union(web_students))
# print(py_students | web_students)

# intersection() keeps only the students present in both sets.
print(py_students.intersection(web_students))
# print(py_students & web_students)

# difference() removes common students from the first set.
print(py_students.difference(web_students))
# print(py_students - web_students)

# Reversing the order shows the students unique to the web group.
print(web_students.difference(py_students))
# print(web_students - py_students)