# Part 1 - Factorial 
# If you enter number like 'ten' or 'six' it will create an error
# To solve this you use Exception Handling (try-except):
num = input("Enter a number: ")
n = int(num)
fact = 1
for i in range(1,n+1):
    fact = fact * i
print("Factorial of",n,"=",fact)

# Part 2 - Addition
x = 10
y = 20
sum = x + y
print(sum)