# Slicing lets us get a section of a list.
# The syntax list[start:end] includes items from start up to, but not including, end.

numbers = [10,20,30,40,50,60]  # Create a list of six numbers.
print(numbers[0:4])  # Print items from index 0 through index 3.

# Omit the starting index to begin from the first element.
print(numbers[:4])  # Print the first 4 items.

# Omit the ending index to go to the end of the list.
print(numbers[2:])  # Print items from index 2 to the end.

# Negative indexing starts counting from the end of the list.
print(numbers[-3:])  # Print the last 3 items.

# A third value in slicing is the step size: start:end:step.
print(numbers[0:5:2])  # Print every second item from index 0 to 4.

# When step is omitted, it defaults to 1.
print(numbers[::2])  # Print every second item in the full list.

# Copying a list using a full slice creates a separate copy.
numbers_copy = numbers[:]  # Copy all items to a new list.
print(numbers_copy)  # Display the copied list.

# Reversing a list with a negative step.
reverse_numbers = numbers[::-1]  # Start at the end and move backward.
print(reverse_numbers)  # Show the reversed list.

# The original list remains unchanged because slicing creates a new list.
print(numbers)  # Display the original list again.

