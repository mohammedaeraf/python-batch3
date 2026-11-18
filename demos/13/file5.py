course = input("Enter Course Name: ")
with open("courses.txt","a") as f:
    f.write(course)
    f.write("\n")