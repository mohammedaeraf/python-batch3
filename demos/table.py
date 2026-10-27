# Multiplication Table using while loop
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    result = n * i
    print(n,"x",i,"=",result)
    i = i + 1