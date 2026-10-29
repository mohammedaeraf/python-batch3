# Tables of numbers from 1 to 20
n = 1
while n <= 20:
    print("***** Table of",n,"*****")
    i = 1
    while i <= 10:
        print(n,"x",i,"=",n * i)
        i = i + 1
    print()
    n = n + 1