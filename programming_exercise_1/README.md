# Programming Exercise 1: Multi-dimensional List Analysis

Given the multi-dimensional list:
```python
[[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
```

1. using PYTHON 3 and pandas
	1. Sum of all numbers
	2. Average of all numbers
	3. Sum of all even numbers
	4. Average of all even numbers
2. do again WITHOUT pandas (plain python, no pandas, no numpy, no other library)
	1. Sum of all numbers
	2. Average of all numbers
	3. Sum of all even numbers
	4. Average of all even numbers


## 1. Key Points I Realized

### The Main Problem: Irregular Data Structure
The multi-dimensional list has **irregular shapes**:
**This creates a fundamental problem:** We cannot create a regular NumPy array because all rows must have the same length. The shape `[4, 3, 4, 4]` is inhomogeneous.

### Additional Challenges:
- Need to handle missing data points
- Must flatten the irregular structure
- Need to filter for even numbers

## 2. How I Solved It

### Solution 1: Using Pandas (`with_pandas.py`)

**Why I chose DataFrame:**
- **Handles irregular data:** DataFrames can automatically fill missing values with NaN
- **Built-in NaN handling:** No need to manually manage missing data
- **Rich functionality:** Built-in methods for calculations and filtering

**What is the different between `stack()` and `flatten()`:**
- **`flatten()` (NumPy):** Includes ALL values (including NaN) → `[11, 12, 5, 2, 15, 6, 10, NaN, 10, 8, 12, 5, 12, 15, 8, 6]`
- **`stack()` (Pandas):** Automatically removes NaN values → `[11, 12, 5, 2, 15, 6, 10, 10, 8, 12, 5, 12, 15, 8, 6]`

### Solution 2: Plain Python (`no_pandas.py`)

**How I handled the irregular structure:**

- **Manual flattening using nested loops:** The outer loop iterates through each row in the multi-dimensional list, while the inner loop extracts each value from the current row
```python
all_numbers = []
for row in data:
    for num in row:
        all_numbers.append(num)
```

- **Manual filtering for even numbers:** Iterate through all numbers and use the modulo operator to identify values divisible by 2
```python
even_numbers = []
for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
```

## Results
- Sum of all numbers: 137.0
- Average of all numbers: 9.13
- Sum of even numbers: 86.0
- Average of even numbers: 8.6
