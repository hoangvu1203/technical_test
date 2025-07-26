import pandas as pd

# Create a multi-dimensional list to store data
data = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

# Convert to a pandas DataFrame, filling missing values with NaN, 
df = pd.DataFrame(data)

# Flatten all numbers into a single Series, ignoring NaNs
all_numbers = df.stack()

# Create even numbers series by checking divided by 22
even_numbers = all_numbers[all_numbers % 2 == 0]

# 1. Sum of all numbers
total_sum = all_numbers.sum()
# 2. Average of all numbers
total_avg = all_numbers.mean()
# 3. Sum of all even numbers
even_sum = even_numbers.sum()
# 4. Average of all even numbers
even_avg = even_numbers.mean()

# Display results
print("Using pandas:")
print(f"1. Sum of all numbers: {total_sum}")
print(f"2. Average of all numbers: {total_avg}")
print(f"3. Sum of all even numbers: {even_sum}")
print(f"4. Average of all even numbers: {even_avg}")
