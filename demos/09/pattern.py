def pattern(ch, times):
    i = 1
    while i <= times:
        print(ch, end="")
        i = i + 1
    print()

    
pattern("*",5)
pattern("#",50)