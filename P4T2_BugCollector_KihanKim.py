# Write a program that keeps a running total of the number of bugs collected during five days.
# October 18, 2019
# CTI-110 P4T2 - Bug Collector
# Kihan Kim

total = 0
for day in range(1,6):
    print('Enter the number of bugs collected on day', day,':')
    bugs = int(input())
    total+= bugs
print('You collected a total of', total, ' bugs.')


# Initialize an accumulator variable
# Obtain number of bugs collected for each day
# Prompt User
# Get number of bugs and accumulate them
# Display total number of bugs
