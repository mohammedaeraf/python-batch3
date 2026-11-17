students = [
    {"name": "Ahmed", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Rahul", "marks": 28},
    {"name": "Ali", "marks": 85},
    {"name": "Fatima", "marks": 92},
    {"name": "Joseph", "marks": 76},
]

searchStudent = input("Enter student's name: ")

for student in students:
    if student.get("name") == searchStudent:
        print(student)