student = ("Isa Khan",23,"Advanced Web Design")
# student[1] = 24 # will cause an error
print(student)

fruits = ("apple","banana","orange","lemon")
print(fruits[0])

# loop and print one fruit in a line
for fruit in fruits:
    print(fruit)

# check if fruits exist
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print(fruit, "is present in", fruits)
else:
    print(fruit, "is not present in", fruits)
