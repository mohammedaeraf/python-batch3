students = ["Ali","Maryam","Fatima","Rohan","Ramesh","Owais","Sunita"]

studentName = input("Enter student name to check in the list:")

if studentName in students:
    print(studentName, "is present in the Database")
else:
    print(studentName, "is not present in the Database")
