# Create a list containing the table of 5

# Method 1
print("\nMethod 1")

a = 5
table = []

for i in range(1, 11):
    table.append(5 * i)

print(table)

# Method 2
print("\nMethod 2")

table = [5 * i for i in range(1, 11)]
print(table)

