# Write a program that uses nested loops to draw this pattern:
# October 19, 2019
# CTI-110 P4HW3 - Nested Loops
# Kihan Kim

num_steps = 6

for n in range(num_steps):
    print('#', end='')
    for c in range(n):
        print(' ', end='')
    print('#')


# Initialize variable for maximum number
# Create loop
# Display number of rows of pound sign
# Display space between pound sign
# Display second pound sign in each row
