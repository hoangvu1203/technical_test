# Custom mean function
def mean(lst):
    total = 0
    for x in lst:
        total += x
    return total / len(lst)

# Custom variance function (sample variance, n-1 in denominator)
def variance(lst):
    m = mean(lst)
    squared_diffs = [(x - m) ** 2 for x in lst]
    return sum(squared_diffs) / (len(lst) - 1)

# Custom standard deviation function
def std_dev(lst):
    return variance(lst) ** 0.5

# Initialize variables to store data    
MedicalTests = {                                # Dictionary of medical test results
    'Cholesterol': [4.32, 3, 2],
    'Sugar': [3.45, 5, 6],
    'Enzyms': [2, 5.67, 4],
    'Calcium': [5.63, 4.67, 6]
}
all_values = []                                 # Initialize an empty list to store all values

# Data Preprocessing
for values in MedicalTests.values():            # Flatten the dictionary into a list of all values
    all_values.extend(values)

# Calculation
global_avg = mean(all_values)                   # Calculate the global average of all values

test_results = {}                               # Initialize an empty dictionary to store the statistics per test
for test, values in MedicalTests.items():       # Calculate the statistics per test
    test_results[test] = {
        'mean': mean(values),
        'max': max(values),
        'min': min(values),
        'variance': variance(values),
        'std_dev': std_dev(values)
    }

# Display results
print(f"Global average: {global_average:.2f}")  # Print the global average

print("\nStatistics per test:")                 # Print the statistics per test
for test, stats in test_results.items():        # Print all the stored results
    print(f"\n{test}:")
    print(f"  Mean: {round(stats['mean'], 2)}")
    print(f"  Max: {stats['max']}")
    print(f"  Min: {stats['min']}")
    print(f"  Variance: {round(stats['variance'], 4)}")
    print(f"  Standard Deviation: {round(stats['std_dev'], 2)}")