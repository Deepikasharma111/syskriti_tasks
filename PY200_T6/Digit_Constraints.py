# Get the range limit N from the user
n = int(input("Enter the value of N: "))

# Initialize a variable to track if we found a match
found_number = -1

# Loop through every number from 1 to N
for x in range(1, n + 1):
    # Convert number to string to easily check digits
    s_x = str(x)
    
    # Rule 1: Sum of digits is divisible by 7
    digit_sum = sum(int(digit) for digit in s_x)
    is_divisible_by_7 = (digit_sum % 7 == 0)
    
    # Rule 2: Contains exactly two 3s
    has_two_threes = (s_x.count('3') == 2)
    
    # Rule 3: Does not contain digit 0
    has_no_zero = ('0' not in s_x)
    
    # Check if all rules are satisfied
    if is_divisible_by_7 and has_two_threes and has_no_zero:
        found_number = x
        break  # Stop at the first (smallest) one found

# Print the result
print(found_number)
