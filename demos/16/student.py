class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name =", self.name)
        print("Age =", self.age)


student1 = Student("Ali",19)
student2 = Student("Fatima",18)

student1.display()

