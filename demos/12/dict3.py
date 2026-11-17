students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Rahul", "marks": 28}
]

for student in students:
    if student.get("marks") >= 40:
        print(student.get("name"), "- Pass")
    else:
        print(student.get("name"), "- Fail")

print(students[0])
