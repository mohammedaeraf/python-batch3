marks = [90,45,69,73,100]

totalMarks = 0
for mark in marks:
    totalMarks = totalMarks + mark

print("Total Marks =",totalMarks)

# Second method
totalMarks2 = sum(marks)
print("Total Marks (2nd method) = ", totalMarks2)

print("Max Marks =>", max(marks))
print("Min Marks =>", min(marks))
