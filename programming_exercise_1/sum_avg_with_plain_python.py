# Create a multi-dimensional list to store data
data = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

# Initialize an empty list to store all numbers
all_numbers = []    
# Flatten all numbers into a single Series
for row in data:
    for num in row:
        all_numbers.append(num) 

# Initialize an empty list to store even numbers
even_numbers = []
# Check if the number is even
for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# 1. Sum of all numbers
total_sum = sum(all_numbers)
# 2. Average of all numbers by dividing the sum by the number of elements
total_avg = sum(all_numbers) / len(all_numbers)
# 3. Sum of all even numbers
even_sum = sum(even_numbers)
# 4. Average of all even numbers by dividing the sum by the number of elements
even_avg = sum(even_numbers) / len(even_numbers)

# Display results
print("Using no pandas:")
print(f"1. Sum of all numbers: {total_sum}")
print(f"2. Average of all numbers: {total_avg}")
print(f"3. Sum of all even numbers: {even_sum}")
print(f"4. Average of all even numbers: {even_avg}")
