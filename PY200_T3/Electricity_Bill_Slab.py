# Get the units from the user
units = float(input("Enter the total electricity units consumed: "))

bill = 0

if units > 0:
    # Always add the fixed charge if consumption is greater than 0
    bill += 50
    
    if units <= 100:
        bill += units * 2
    elif units <= 200:
        # First 100 units at 2, remaining units at 3
        bill += (100 * 2) + (units - 100) * 3
    elif units <= 500:
        # First 100 at 2, next 100 at 3, remaining units at 5
        bill += (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        # First 100 at 2, next 100 at 3, next 300 at 5, remaining at 8
        bill += (100 * 2) + (100 * 3) + (300 * 5) + (units - 500) * 8

    print(f"Total Electricity Bill: {bill}")
else:
    print("Units must be greater than 0 for a bill to be generated.")
