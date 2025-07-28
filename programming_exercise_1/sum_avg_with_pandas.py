import pandas as pd

# Initialize lists to store data
data = [[11, 12, 5, 2], 
        [15, 6, 10], 
        [10, 8, 12, 5], 
        [12, 15, 8, 6]]                             # Initialize a multi-dimensional list to store data
all_numbers = []                                    # Initialize an empty list to store all numbers
even_numbers = []                                   # Initialize an empty list to store even numbers

# Data Preprocessing
df = pd.DataFrame(data)                             # Convert to a pandas DataFrame, filling missing values with NaN
all_numbers = df.stack()                            # Flatten all numbers into a single Series, ignoring NaNs
even_numbers = all_numbers[all_numbers % 2 == 0]    # Check if the number is even

# Calculation
total_sum = all_numbers.sum()                       # Sum of all numbers
total_avg = all_numbers.mean()                      # Average of all numbers
even_sum = even_numbers.sum()                       # Sum of all even numbers
even_avg = even_numbers.mean()                      # Average of all even numbers

# Display results
print("Using pandas:")
print(f"1. Sum of all numbers: {total_sum}")
print(f"2. Average of all numbers: {total_avg}")
print(f"3. Sum of all even numbers: {even_sum}")
print(f"4. Average of all even numbers: {even_avg}")
