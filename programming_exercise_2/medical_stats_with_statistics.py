import statistics
from tabulate import tabulate

# Function implementations
def flatten_list(data, res_list):
    """
    Flatten a multi-dimensional list into a single list
    data: multi-dimensional list
    Returns: flattened list
    """
    for row in data:                              
        res_list.extend(row)                                     # Add all numbers from the row at once
    return res_list

def format_results_table(test_results):
    """
    Format medical test results into a table string
    test_results: dictionary with test names and their statistics
    Returns: formatted table as string
    """
    # Initialize empty table data
    table_data = []
    # Header
    headers = ['', 'mean', 'max', 'min', 'std', 'var']

    # Data rows
    for test, stats in test_results.items():
        row = [
            test,
            stats['mean'],
            stats['max'],
            stats['min'],
            stats['std_dev'],
            stats['variance']
        ]
        table_data.append(row)

    return tabulate(table_data, headers=headers, tablefmt="simple", floatfmt=".2f") 

# Main execution
if __name__ == "__main__":
    # Initialize variables to store data
    MedicalTests = {                                             # Dictionary of medical test results
        'Cholesterol': [4.32, 3, 2],
        'Sugar': [3.45, 5, 6],
        'Enzyms': [2, 5.67, 4],
        'Calcium': [5.63, 4.67, 6]
    }
    all_values = []                                              # Initialize an empty list to store all values

    # Data Preprocessing    
    all_values = flatten_list(MedicalTests.values(), all_values) # Flatten the dictionary into a list of all values

    # Calculation
    global_avg = statistics.mean(all_values)                     # Calculate the global average of all values

    test_results = {}                                            # Initialize an empty dictionary to store the statistics per test
    for test, values in MedicalTests.items():                    # Calculate the statistics per test
        test_results[test] = {
            'mean': statistics.mean(values),
            'max': max(values),
            'min': min(values),
            'std_dev': statistics.stdev(values),
            'variance': statistics.variance(values)
        }

    # Formatting the results
    table_results = format_results_table(test_results)

    # Display results
    print(f"Global average: {global_avg:.2f}")                   # Print the global average
    print("\nStatistics per test:")                              # Print the statistics per test
    print(table_results)                                         # Print all the stored results using the new formatting function   