# Get the grid size from the user
n = int(input("Enter the size of the grid (N): "))

# Loop through each row
for row in range(n):
    # Loop through each column in that row
    for col in range(n):
        # 1. First, check the special "X" condition
        if row == col:
            print("X", end=" ")
        
        # 2. If not an X, check the even/odd logic for 1 or 0
        elif (row + col) % 2 == 0:
            print("1", end=" ")
        
        # 3. Otherwise, print 0
        else:
            print("0", end=" ")
            
    # After each row is finished, print a newline
    print()
