# Programming Exercise 2: Medical Tests Statistical Analysis

Given a dictionary of medical test results:
```python
MedicalTests = {
    'Cholesterol': [4.32, 3, 2],
    'Sugar': [3.45, 5, 6],
    'Enzyms': [2, 5.67, 4],
    'Calcium': [5.63, 4.67, 6]
}
```

Calculate the following statistics:
1. **Global average** of all values
2. **Per-test statistics** for each medical test:
   - Mean
   - Maximum
   - Minimum
   - Standard Deviation
   - Variance

## 1. Key Points I Realized

### The Main Challenge: Data Structure Transformation
The data comes as a **dictionary with lists as values**, which is not ideal for statistical analysis:
- **Input format:** `{'Test': [value1, value2, value3], ...}`
- **Problem:** Dictionary structure doesn't support vectorized operations
- **Need:** Convert to a format that supports statistical calculations

## 2. How I Solved It
The solution 1 is the best solution, the other 2 solution is just a test I try to figure out different ways to solve problem, and have a overview to compare.

### I follow this structure
1. Import libraries and create custom function if needed
2. Initialize variables to store data
3. Preprocesing the data (flatten)
4. Calculate the results
5. Formatting the results for better display
6. Display the results

### Solution 1: Using Pandas & NumPy (`using_numpy_pandas.py`)

**Why I chose DataFrame transformation:**
- **Dictionary → DataFrame:** Converts the data structure to a tabular format
- **Column-based operations:** Each test becomes a column, enabling vectorized calculations
- **Built-in statistical methods:** Pandas provides all needed statistical functions
- **Professional output:** DataFrame formatting makes results easy to read

**Why I used `df.stack()` for global average:**
- **Flattens all data:** Converts the 2D DataFrame into a 1D Series
- **Handles irregular data:** Works even if tests have different numbers of measurements

**Why I used `agg()` method:**
- **Multiple functions at once:** Applies all statistical functions in one operation
- **Consistent output:** Returns a well-formatted DataFrame with all statistics
- **Efficient:** Avoids multiple separate calculations
- **Professional presentation:** Results are organized in a clear table format

### Solution 2: Using statistics library

**Simple built-in approach:**
- Uses Python's built-in `statistics` module for calculations and `tabulate` for table format display

### Solution 3: Using plain python 

**Custom implementation approach:**
- Implements all statistical functions from scratch (mean, variance, standard deviation)
- Understanding of mathematical formulas behind the statistics
- Uses only basic Python operations and built-in functions

## 3. Results
```
1. Global average of all values: 4.25

2. Statistics per test:
             mean   max   min   std   var
Cholesterol  3.11  4.32  2.00  1.16  1.35
Sugar        4.82  6.00  3.45  1.28  1.65
Enzyms       3.89  5.67  2.00  1.84  3.38
Calcium      5.43  6.00  4.67  0.69  0.47
```

