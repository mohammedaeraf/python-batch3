# Nested Loops (A loop within a loop)
# Factorial of numbers from 2 to 10
for n in range(2,11):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print("Factorial of",n,"=",fact)
