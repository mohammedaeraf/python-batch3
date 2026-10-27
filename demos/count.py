# Count Odd & Even Nos in a range
start = 21
end = 29
odd_count = 0
even_count = 0

i = start
while i <= end:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    i = i + 1
        
print("Odd Nos Count =", odd_count)
print("Even Nos Count =", even_count)

