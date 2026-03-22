# Mean, Median, Mode using basic constructs (no inbuilt functions)

# Input list
numbers = [10, 20, 30, 40, 20, 10, 50]

# -------- MEAN --------
total = 0
count = 0

for num in numbers:
    total = total + num
    count = count + 1

mean = total / count
print("Mean:", mean)


# -------- MEDIAN --------
# Step 1: Sort list manually (Bubble Sort)
n = count

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Step 2: Find median
if n % 2 == 0:
    mid1 = numbers[n // 2]
    mid2 = numbers[(n // 2) - 1]
    median = (mid1 + mid2) / 2
else:
    median = numbers[n // 2]

print("Median:", median)


# -------- MODE --------
mode = numbers[0]
max_count = 0

for i in range(n):
    current = numbers[i]
    freq = 0

    for j in range(n):
        if numbers[j] == current:
            freq = freq + 1

    if freq > max_count:
        max_count = freq
        mode = current

print("Mode:", mode)
