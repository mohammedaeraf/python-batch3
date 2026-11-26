import numpy 

marks_list = [75, 80, 90, 65, 80]
marks = numpy.array(marks_list)

print("Total Marks: ", numpy.sum(marks))
print("Avg Marks: ", numpy.mean(marks))
print("Highest Marks: ", numpy.max(marks))
print("Lowest Marks: ", numpy.min(marks))
print("Sorted Marks", numpy.sort(marks))

print("Bonus:", marks+5)
print("Deduce:", marks-5)
print("Double:", marks*2)
print("Percent Increase:", marks*1.10)
print("Number of Elements:", marks.size)