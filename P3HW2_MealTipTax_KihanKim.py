# CTI-110
# P3HW2 - MealTipTax
# Kihan Kim
# October 4, 2019
#
meal = float(input('Enter the charge for the meal: '))
sales_tax = .06
tip = int(input('Please select a tip percentage (16% or 18% or 20%): ')) / 100
tip_calc = tip * meal

sales_tax_calc = sales_tax * meal
total_cost = meal + tip_calc + sales_tax_calc

if tip == .16:
    print('The calculated tip is $', format(tip_calc, '.2f'), sep= '')
    print('The calculated tax is $', format(sales_tax_calc, '.2f'), sep= '')
    print('The total cost of your meal is $', format(total_cost, ',.2f'), sep= '')
elif tip == .18:
    print('The calculated tip is $', format(tip_calc, '.2f'), sep= '')
    print('The calculated tax is $', format(sales_tax_calc, '.2f'), sep= '')
    print('The total cost of your meal is $', format(total_cost, ',.2f'), sep= '')
elif tip == .20:
    print('The calculated tip is $', format(tip_calc, '.2f'), sep= '')
    print('The calculated tax is $', format(sales_tax_calc, '.2f'), sep= '')
    print('The total cost of your meal is $', format(total_cost, ',.2f'), sep= '')
else:
    print('Error! Please select the correct tip percentage')


# Get the charge for the meal
# Get the tip selected for meal
# If tip selected is another percentage:
#   Display error code
# Calculate tip
# Calculate tax
# Calculate total cost of meal
# Display total cost of meal
        
