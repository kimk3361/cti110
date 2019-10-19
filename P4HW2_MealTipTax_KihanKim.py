# CTI-110
# P4HW2 - MealTipTax
# Kihan Kim
# October 18, 2019
#
another = 'y'
while another == 'y' or another == 'Y':
    meal = float(input('Enter the charge for the meal: '))
    tip = float(input('Please select a tip (16% or 18% or 20%): '))
    while tip != .16 and tip != .18 and tip != .20:
        print('You must enter a valid tip! (Example: enter .18 instead of 18%)')
        tip = float(input('Please enter a correct tip (Example: enter .18 instead of 18%): '))
    sales_tax = .06
    sales_tax_calc = sales_tax * meal
    tip_calc = tip * meal
    total_cost = meal + tip_calc + sales_tax_calc
    print('The calculated tip is $', format(tip_calc, '.2f'), sep= '')
    print('The calculated tax is $', format(sales_tax_calc, '.2f'), sep= '')
    print('The orginial cost of your meal is $', format(meal, '.2f'), sep= '')
    print('The total cost of your meal is $', format(total_cost, '.2f'), sep= '')   
    another = input('Would you like to try again? (y/n): ')
# Initialize control variable for loop
# Get the charge for the meal
# Get the tip selected for meal
# If tip selected is another percentage or integer:
    # Display error code
    # Ask for correct tip
# Calculate and display tip
# Calculate and display tax
# Calculate total cost of meal
# Display original cost of meal
# Display total cost of meal
# Ask if user would like to try again


