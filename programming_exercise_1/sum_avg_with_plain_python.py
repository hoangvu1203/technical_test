# Table formatting function 
def format_results_table(data_dict):
    """
    Format results into a table string
    data_dict: dictionary with format {'row_name': [sum_value, avg_value]}
    Returns: formatted table as string
    """
    # Header
    result = f"{'':^8}{'Sum':^8}{'Average':^8}\n"
    
    # Data rows
    for row_name, values in data_dict.items():
        sum_val, avg_val = values
        result += f"{row_name:^8}{sum_val:^8.2f}{avg_val:^8.2f}\n"

    return result.rstrip()                           # Remove trailing newline

# Flatten function 
def flatten_list(data, res_list):
    """
    Flatten a multi-dimensional list into a single list
    data: multi-dimensional list
    Returns: flattened list
    """
    for row in data:                              
        for num in row:
            res_list.append(num) 
    return res_list

# Get even function
def get_even(data, res_list):
    """
    Check if a number is even
    num: number
    Returns: True if the number is even, False otherwise
    """
    for num in data:
        if num % 2 == 0:
            res_list.append(num)
    return res_list

# Initialize lists to store data
data = [[11, 12, 5, 2],                             # Initialize a multi-dimensional list to store data
        [15, 6, 10], 
        [10, 8, 12, 5], 
        [12, 15, 8, 6]]         
all_numbers = []                                    # Initialize an empty list to store all numbers
even_numbers = []                                   # Initialize an empty list to store even numbers

# Data Preprocessing
all_numbers = flatten_list(data, all_numbers)       # Flatten all numbers into a single Series
even_numbers = get_even(all_numbers, even_numbers)  # Get even numbers

# Calculation
total_sum = float(sum(all_numbers))                 # Sum of all numbers
total_avg = sum(all_numbers) / len(all_numbers)     # Average of all numbers
even_sum = float(sum(even_numbers))                 # Sum of all even numbers
even_avg = sum(even_numbers) / len(even_numbers)    # Average of all even numbers

# Formatting the results
results = format_results_table({                    # Create a results table
    'All': [total_sum, total_avg],
    'Even': [even_sum, even_avg]
})

# Display results
print("Using no pandas:")
print(results)
