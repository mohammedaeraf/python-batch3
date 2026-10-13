# Program to check whether a number is odd or even.
# Read a number from the user and convert it to an integer.
n = int(input("Enter a number: "))

# Find the remainder when the number is divided by 2.
# If the remainder is 0, the number is even; otherwise it is odd.
remainder = n % 2

if remainder == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")

