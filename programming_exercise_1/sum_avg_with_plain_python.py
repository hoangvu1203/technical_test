# Initialize lists to store data
data = [[11, 12, 5, 2],                             # Initialize a multi-dimensional list to store data
        [15, 6, 10], 
        [10, 8, 12, 5], 
        [12, 15, 8, 6]]         
all_numbers = []                                    # Initialize an empty list to store all numbers
even_numbers = []                                   # Initialize an empty list to store even numbers

# Data Preprocessing
for row in data:                                    # Flatten all numbers into a single Series
    for num in row:
        all_numbers.append(num) 

for num in all_numbers:                             # Check if the number is even
    if num % 2 == 0:
        even_numbers.append(num)

# Calculation
total_sum = sum(all_numbers)                        # Sum of all numbers
total_avg = sum(all_numbers) / len(all_numbers)     # Average of all numbers
even_sum = sum(even_numbers)                        # Sum of all even numbers
even_avg = sum(even_numbers) / len(even_numbers)    # Average of all even numbers

# Display results
print("Using no pandas:")
print(f"1. Sum of all numbers: {total_sum}")
print(f"2. Average of all numbers: {total_avg}")
print(f"3. Sum of all even numbers: {even_sum}")
print(f"4. Average of all even numbers: {even_avg}")
