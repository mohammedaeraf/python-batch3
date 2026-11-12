# Multiplication Table using while loop

def print_table(n):
    i = 1
    print(" Table of",n)
    while i <= 10:
        result = n * i
        print(n,"x",i,"=",result)
        i = i + 1
    print()


print_table(13)
print_table(25)

