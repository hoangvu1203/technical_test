import pandas as pd
import numpy as np

# Dictionary of medical test results
MedicalTests = {
    'Cholesterol': [4.32, 3, 2],
    'Sugar': [3.45, 5, 6],
    'Enzyms': [2, 5.67, 4],
    'Calcium': [5.63, 4.67, 6]
}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(MedicalTests)

# 1. Global average of all values
global_avg = df.stack().mean()
print(f"1. Global average of all values: {global_avg:.2f}")

# 2. Statistics per test
summary = df.agg(['mean', 'max', 'min', 'std', 'var'])

print("\n2. Statistics per test:")
print(summary.round(2))
