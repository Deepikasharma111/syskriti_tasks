# Get password input from the user
password = input("Enter your password to check strength: ")

# Initialize our check variables as False
has_upper = False
has_lower = False
has_digit = False
has_length = len(password) >= 8

# Loop through every character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True

# Check if all four rules are met
if has_length and has_upper and has_lower and has_digit:
    print("STRONG")
else:
    print("WEAK")
