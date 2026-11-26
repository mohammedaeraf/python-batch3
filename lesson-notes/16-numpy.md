# NumPy

## 1. What is NumPy?

NumPy stands for **Numerical Python**.

It is a Python library used for:
- Performing mathematical calculations.
- Working with numerical data.
- Creating and manipulating arrays.
- Performing statistical calculations.
- Processing large datasets efficiently.

NumPy is widely used in Data Science, Data Analytics, Machine Learning and Artificial Intelligence.

### Why do we need NumPy?

Python already provides lists to store multiple values. However, NumPy provides specialized arrays that make numerical operations easier and more efficient.

**Example using a Python list:**

```python
marks = [75, 85, 90, 65, 80]

bonus_marks = []

for mark in marks:
    bonus_marks.append(mark + 5)

print(bonus_marks)
```

**Using NumPy:**

```python
import numpy as np

marks = np.array([75, 85, 90, 65, 80])

bonus_marks = marks + 5

print(bonus_marks)
```

Output:

```text
[80 90 95 70 85]
```

Notice that NumPy allows us to perform an operation on all array elements without writing a loop.

This is called **element-wise operation**.

## 2. Installing and Importing NumPy

In Google Colab, NumPy is generally pre-installed.

To use NumPy, import the library:

```python
import numpy as np
```

Here:
- `import` loads a Python library.
- `numpy` is the library name.
- `np` is an alias used to refer to NumPy.

We can now use NumPy functions through `np`.

## 3. Creating NumPy Arrays

A NumPy array is a collection of elements stored in an organized structure.

### A. Creating a one-dimensional array

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

Output:

```text
[10 20 30 40 50]
```

### B. Creating a two-dimensional array

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(matrix)
```

Output:

```text
[[10 20 30]
 [40 50 60]]
```

### C. Creating an array of zeros

```python
zeros = np.zeros(5)

print(zeros)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

### D. Creating an array of ones

```python
ones = np.ones(5)

print(ones)
```

Output:

```text
[1. 1. 1. 1. 1.]
```

### E. Generating a sequence of numbers

```python
numbers = np.arange(1, 11)

print(numbers)
```

Output:

```text
[ 1  2  3  4  5  6  7  8  9 10]
```

Note: The ending value in `np.arange()` is excluded.

## 4. NumPy Array Properties

NumPy provides several properties to understand an array.

```python
import numpy as np

marks = np.array([75, 85, 90, 65, 80])

print("Size:", marks.size)
print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Data Type:", marks.dtype)
```

Output (data type may vary):

```text
Size: 5
Dimensions: 1
Shape: (5,)
Data Type: int64
```

| Property | Description |
|---|---|
| `size` | Returns the total number of elements |
| `ndim` | Returns the number of dimensions |
| `shape` | Returns the size along each dimension |
| `dtype` | Returns the data type of array elements |

## 5. Accessing Array Elements

NumPy supports indexing and slicing, just like Python lists.

```python
import numpy as np

marks = np.array([75, 85, 90, 65, 80])

print(marks[0])      # First element
print(marks[2])      # Third element
print(marks[-1])     # Last element
print(marks[1:4])    # Slicing
```

Output:

```text
75
90
80
[85 90 65]
```

Remember: Array indexing starts from zero.

## 6. Mathematical Operations

NumPy allows us to perform mathematical operations on all elements of an array.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers + 5)
print(numbers - 5)
print(numbers * 2)
print(numbers / 2)
```

Output:

```text
[15 25 35 45 55]
[ 5 15 25 35 45]
[ 20  40  60  80 100]
[ 5. 10. 15. 20. 25.]
```

These operations are performed element by element.

## 7. Statistical Functions

NumPy provides built-in functions to perform statistical calculations.

| Function | Purpose |
|---|---|
| `np.sum()` | Calculates the total |
| `np.mean()` | Calculates the average |
| `np.max()` | Finds the highest value |
| `np.min()` | Finds the lowest value |
| `np.median()` | Finds the median |
| `np.std()` | Calculates standard deviation |
| `np.sort()` | Sorts the array |
| `np.unique()` | Finds unique elements |

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Total:", np.sum(numbers))
print("Average:", np.mean(numbers))
print("Highest:", np.max(numbers))
print("Lowest:", np.min(numbers))
print("Median:", np.median(numbers))
print("Sorted:", np.sort(numbers))
```

Output:

```text
Total: 150
Average: 30.0
Highest: 50
Lowest: 10
Median: 30.0
Sorted: [10 20 30 40 50]
```

## 8. Filtering Array Elements

We can use conditions to filter elements from a NumPy array.

Example:

```python
import numpy as np

marks = np.array([75, 85, 90, 65, 80])

high_marks = marks[marks > 80]

print(high_marks)
```

Output:

```text
[85 90]
```

Explanation:

- `marks > 80` checks every element.
- It produces Boolean values (`True` or `False`).
- `marks[marks > 80]` returns only the elements satisfying the condition.

---

# Practical Example: E-commerce Sales Analysis

## 9. Business Scenario

An e-commerce company records the number of products sold over five days.

The management wants to analyse sales performance and calculate revenue.

We will use NumPy to perform this analysis.

### Step 1: Create the sales array

```python
import numpy as np

# Number of products sold each day
sales = np.array([120, 150, 90, 200, 180])

print("Daily Sales:", sales)
```

Output:

```text
Daily Sales: [120 150  90 200 180]
```

Each number represents the quantity of products sold on a particular day.

### Step 2: Perform mathematical operations

Suppose the company wants to increase its daily sales target by 20 units.

```python
new_target = sales + 20

print("New Sales Target:", new_target)
```

Output:

```text
New Sales Target: [140 170 110 220 200]
```

We can also perform multiplication and division:

```python
print("Double Sales:", sales * 2)

print("Half Sales:", sales / 2)
```

### Step 3: Calculate revenue

Suppose each product costs ₹500.

Revenue = Quantity Sold × Product Price

```python
product_price = 500

revenue = sales * product_price

print("Daily Revenue:", revenue)
```

Output:

```text
Daily Revenue: [ 60000  75000  45000 100000  90000]
```

The company can calculate revenue for all five days using a single multiplication operation.

### Step 4: Perform statistical analysis

The management wants to understand overall sales performance.

```python
print("Total Units Sold:", np.sum(sales))

print("Average Daily Sales:", np.mean(sales))

print("Highest Sales:", np.max(sales))

print("Lowest Sales:", np.min(sales))

print("Median Sales:", np.median(sales))
```

Output:

```text
Total Units Sold: 740

Average Daily Sales: 148.0

Highest Sales: 200

Lowest Sales: 90

Median Sales: 150.0
```

### Step 5: Identify high-performing days

Management wants to identify days when sales exceeded 150 units.

```python
high_sales = sales[sales > 150]

print("High Sales Days:", high_sales)
```

Output:

```text
High Sales Days: [200 180]
```

To count the number of days with sales above 150:

```python
count = np.sum(sales > 150)

print("Number of High Sales Days:", count)
```

Output:

```text
Number of High Sales Days: 2
```

### Step 6: Apply a discount

Suppose the company offers a 10% discount on the product price.

```python
discounted_price = product_price * 0.90

discounted_revenue = sales * discounted_price

print("Discounted Price:", discounted_price)

print("Revenue After Discount:", discounted_revenue)
```

Output:

```text
Discounted Price: 450.0

Revenue After Discount:
[54000. 67500. 40500. 90000. 81000.]
```

### Step 7: Complete Sales Analysis Program

```python
import numpy as np

# Daily product sales
sales = np.array([120, 150, 90, 200, 180])

# Product price
product_price = 500

# Calculate revenue
revenue = sales * product_price

# Display sales information
print("Daily Sales:", sales)

print("Total Units Sold:", np.sum(sales))

print("Average Daily Sales:", np.mean(sales))

print("Highest Sales:", np.max(sales))

print("Lowest Sales:", np.min(sales))

print("Total Revenue:", np.sum(revenue))

print("Days with Sales Above 150:", sales[sales > 150])

print("New Sales Target:", sales + 20)
```

Expected results:

| Metric | Result |
|---|---:|
| Total units sold | 740 |
| Average daily sales | 148 |
| Highest daily sales | 200 |
| Lowest daily sales | 90 |
| Total revenue | ₹3,70,000 |
| Days above 150 units | 2 |

---

# 10. Student Practice Exercise

## Exercise: Supermarket Milk Sales Analysis

A supermarket records the number of milk packets sold over five days.

```python
milk_sales = np.array([85, 110, 95, 140, 120])
```

Write a Python program using NumPy to perform the following tasks:

1. Display the daily milk sales.
2. Calculate the total number of milk packets sold.
3. Calculate average daily sales.
4. Find the highest and lowest sales.
5. Calculate revenue assuming each milk packet costs ₹30.
6. Identify days when sales exceeded 100 packets.
7. Add 10 packets to each day's sales as a new sales target.

### Bonus Challenge

Count the number of days when sales exceeded 100 packets.

---

# 11. Important NumPy Functions – Quick Reference

| Function | Example |
|---|---|
| Create array | `np.array([10, 20, 30])` |
| Create zeros | `np.zeros(5)` |
| Create ones | `np.ones(5)` |
| Generate sequence | `np.arange(1, 10)` |
| Calculate total | `np.sum(arr)` |
| Calculate average | `np.mean(arr)` |
| Find maximum | `np.max(arr)` |
| Find minimum | `np.min(arr)` |
| Find median | `np.median(arr)` |
| Sort values | `np.sort(arr)` |
| Find unique values | `np.unique(arr)` |
| Calculate square root | `np.sqrt(arr)` |

# 12. Key Takeaways

1. NumPy stands for Numerical Python.
2. NumPy is used for numerical computations and data processing.
3. `np.array()` creates a NumPy array.
4. NumPy supports one-dimensional and multidimensional arrays.
5. NumPy allows element-wise mathematical operations.
6. NumPy provides built-in statistical functions.
7. NumPy supports filtering using conditions.
8. NumPy is an important foundation for learning Pandas and Data Analytics.

**Remember:**

- Python Lists are general-purpose collections.
- NumPy Arrays are designed for efficient numerical computations.
- Pandas DataFrames are designed for structured data analysis.