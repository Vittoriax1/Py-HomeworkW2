# Created by Jennifer Souvannasing, SEC 290, Week 2 Programming Assignment, 07/11/22

# Introductory paragraph
print('Automobile Fuel Cost Calculator')
print(' ')
print('This program may help you decide which car makes sense for you based on your budget.')
print('You will be asked to enter the MPG for the car that you have in mind, the average ')
print('number of miles that you expect to drive each month, and the cost per gallon of fuel.')
print(' ')
print('The program will then calculate the monthly fuel cost.')
print(' ')
miles_per_gallon = float(input('   Please enter the car\'s MPG (miles per gallon): '))
miles_per_month = float(input('   Please enter the average miles driven per month: '))
avg_fuel_cost = float(input('   Please enter the cost of fuel per gallon: $'))
print(' ')

# Calculations
gal_per_mon = miles_per_month / miles_per_gallon
cost_per_mon = gal_per_mon * avg_fuel_cost

# Results
print('Given the price of fuel at ${:.2f} and {:,.2f} miles/month traveled:'.format(avg_fuel_cost, miles_per_month))
print(' ')
print('   Gallons used per month: {:.1f} gallons'.format(gal_per_mon))
print('   Monthly cost of fuel: ${:,.2f}'.format(cost_per_mon))
print(' ')
