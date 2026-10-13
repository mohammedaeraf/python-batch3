# Read two numbers from the user.
# input() always returns a string, so we convert them to integers.
x = int(input("Enter a number: "))
y = int(input("Enter second number: "))

# Addition: adds the two numbers together
sum = x + y
print("Addition =", sum)

# Difference: subtracts the second number from the first
difference = x - y
print("Difference =", difference)

# Product: multiplies the two numbers
product = x * y
print("Product =", product)

# Division: divides the first number by the second
# We check for zero to avoid an error in Python
if y != 0:
    division = x / y
    print("Division =", division)
else:
    print("Division = undefined (cannot divide by zero)")

