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

### Solution: Using Pandas & NumPy (`using_numpy_pandas.py`)

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

## 3. Results
```
1. Global average of all values: 4.25

2. Statistics per test:
        Cholesterol  Sugar  Enzyms  Calcium
mean          3.11   4.82    3.89     5.43
max           4.32   6.00    5.67     6.00
min           2.00   3.45    2.00     4.67
std           1.16   1.28    1.84     0.67
var           1.35   1.63    3.38     0.45
```

