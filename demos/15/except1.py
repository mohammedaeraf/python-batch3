#Part 1 - Factorial
num = input("Enter a number: ")
try:
    n = int(num)
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("Factorial of",n,"=",fact)
except:
    print("Invalid input")

# Part 2 - Addition
x = 10
y = 20
sum = x + y
print(sum)