# Factorial Program
# 4! = 24  (1 x 2 x 3 x 4)
# 5! = 120 (1 x 2 x 3 x 4 x 5)
# Logical Thinking Ability

n = int(input("Enter a number: "))
fact = 1

for i in range(1,n+1):
    fact = fact * i
    # print(fact)

print("Factorial of",n,"=",fact)