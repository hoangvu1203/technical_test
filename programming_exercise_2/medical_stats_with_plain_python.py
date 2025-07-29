# Custom mean function
def mean(lst):
    """
    Calculate the mean of a list of numbers
    lst: list of numbers
    Returns: mean of the list
    """
    total = 0
    for x in lst:
        total += x
    return total / len(lst)

# Custom variance function (sample variance, n-1 in denominator)
def variance(lst):
    """
    Calculate the variance of a list of numbers
    lst: list of numbers
    Returns: variance of the list
    """
    m = mean(lst)
    squared_diffs = [(x - m) ** 2 for x in lst]
    return sum(squared_diffs) / (len(lst) - 1)

# Custom standard deviation function
def std_dev(lst):
    """
    Calculate the standard deviation of a list of numbers
    lst: list of numbers
    Returns: standard deviation of the list
    """
    return variance(lst) ** 0.5

# Table formatting function
def format_results_table(test_results):
    """
    Format medical test results into a table string
    test_results: dictionary with test names and their statistics
    Returns: formatted table as string
    """
    # Header
    result = f"{'':^12}{'mean':^8}{'max':^8}{'min':^8}{'std':^8}{'var':^8}\n"
    
    # Data rows
    for test, stats in test_results.items():
        result += f"{test:^12}{stats['mean']:^8.2f}{stats['max']:^8.2f}{stats['min']:^8.2f}{stats['std_dev']:^8.2f}{stats['variance']:^8.2f}\n"
    
    return result.rstrip()                      # Remove trailing newline

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
        'mean': float(mean(values)),
        'max': float(max(values)),
        'min': float(min(values)),
        'variance': float(variance(values)),
        'std_dev': float(std_dev(values))
    }

# Formatting the results
table_results = format_results_table(test_results)

# Display results
print(f"Global average: {global_avg:.2f}")      # Print the global average
print("\nStatistics per test:")                 # Print the statistics per test
print(table_results)                            # Print all the stored results using the new formatting function