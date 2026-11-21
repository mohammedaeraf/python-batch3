try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter second number: "))
    div = n1/n2
    print(div)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero.")