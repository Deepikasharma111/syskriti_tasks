# 1. Ask the user for input
user_input = input("Please enter a number: ")

# 2. Convert that text into a number
number = float(user_input)

# 3. Logic to check the value
if number < 0:
    # Using abs() to get the positive (absolute) value
    positive_value = abs(number)
    print(f"Your entered number {number} was negative, however positive value of your number is {positive_value}")

elif number > 0:
    print(f"The number {number} is positive.")

else:
    print("The number is zero.")
