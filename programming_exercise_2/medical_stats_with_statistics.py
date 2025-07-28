import statistics

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
global_average = statistics.mean(all_values)    # Calculate the global average of all values

test_results = {}                               # Initialize an empty dictionary to store the statistics per test
for test, values in MedicalTests.items():       # Calculate the statistics per test
    test_results[test] = {
        'mean': statistics.mean(values),
        'max': max(values),
        'min': min(values),
        'std_dev': statistics.stdev(values),
        'variance': statistics.variance(values)
    }

# Display results
print(f"Global average: {global_average:.2f}")  # Print the global average

print("\nStatistics per test:")                 # Print the statistics per test
for test, stats in test_results.items():        # Print all the stored results
    print(f"\n{test}:")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Max: {stats['max']}")
    print(f"  Min: {stats['min']}")
    print(f"  Standard Deviation: {stats['std_dev']:.2f}")
    print(f"  Variance: {stats['variance']:.4f}")