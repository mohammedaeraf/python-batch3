name = "Arif Attar"
password = "Hoiu44#$"
# Indexing selects one character; slicing selects a range of characters.
print(name[0])
print(password[2:5])

course = "Data Analytics Course using Python, Numpy, Pandas, Mathplotlib, Excel and PowerBI"
# A string can be iterated over one character at a time.
for letter in course:
    print(letter)

# The `in` operator checks whether a substring occurs in a string.
if "Excel" in course:
    print("Excel is there in course name")
else:
    print("Excel isn't there in course name")

productTitle = "Round-neck Tshirt (black)"
# These methods return versions of the string with different capitalization.
print(productTitle.upper())
print(productTitle.lower())
print(productTitle.capitalize())

# `replace` returns a copy with matching text substituted.
print(productTitle.replace("Round-neck","V-neck"))

# `count` returns how many times the given substring appears.
count = course.count("o")
print("Occurence of o in course title =>", count)
