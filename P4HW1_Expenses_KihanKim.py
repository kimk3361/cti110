# CTI-110
# P4HW1 - Expenses
# Kihan Kim
# October 18, 2019

another = 'y'
total = 0.0
num_expense = 0
account = float(input('Enter the starting amount in the account' + 
                     'you wish to withdraw from: '))
while another == 'y' or another == 'Y':
    expense = float(input('Enter expense: '))
    total+= expense
    num_expense += 1
    another = input('Do you want to enter another expense? (y/n) ')

print('Amount in account before expense subtraction is ', account)
print('Number of expenses entered is ', num_expense)
after = account - total
print('Amount in account AFTER expenses subtracted is', after)


# Initialize variable to control loop
# Initialize accumulator variables
# Prompt user to enter amount in account
# Prompt user to enter expenses
# Prompt user to enter another expense
# Display original amount
# Display number of expenses
# Calculate amount in account after expenses
# Display amount after expenses
