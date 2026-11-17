student = {
    "name":"Usman Khan",
    "age":18,
    "course":"Python",
    "marks":78.5,
    "active":True,
}

print(student["name"])
print(student.get("name"))

student["age"] = 21

student["email"] = "usman@gmail.com"
print(student)

if "course" in student:
    print("Course Info is present")
else:
    print("Course Info is not present")

print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, "=", value)


