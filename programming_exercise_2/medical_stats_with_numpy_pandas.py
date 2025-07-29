import pandas as pd
import numpy as np

# Initialize variables to store data
MedicalTests = {                                            # Dictionary of medical test results
    'Cholesterol': [4.32, 3, 2],
    'Sugar': [3.45, 5, 6],
    'Enzyms': [2, 5.67, 4],
    'Calcium': [5.63, 4.67, 6]
}
all_values = []                                             # Initialize an empty list to store all values

# Data Preprocessing 
df = pd.DataFrame(MedicalTests)                             # Convert dictionary to pandas DataFrame
all_values = df.stack()                                     # Flatten the DataFrame into a Series

# Calculation
global_avg = all_values.mean()                              # Calculate the global average of all values
test_results = df.agg(['mean', 'max', 'min', 'std', 'var']) # Calculate the statistics per test

# Formatting the results
table_results = test_results.transpose().round(2)           # Transpose the DataFrame and round the values to 2 decimal places

# Display results
print(f"Global average of all values: {global_avg:.2f}")    # Print the global average
print("\nStatistics per test:")                             # Print the statistics per test
print(table_results)                                  
