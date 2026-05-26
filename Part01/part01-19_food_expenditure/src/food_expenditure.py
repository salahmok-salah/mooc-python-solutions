# Write your solution here
mealcount=float(input('How many times a week do you eat at the student cafeteria?'))
mealprice=float(input('The price of a typical student lunch?'))
groceriesprice=float(input('How much money do you spend on groceries in a week?'))
print('Average food expenditure:')
weeklycal=groceriesprice+(mealcount*mealprice)
daily=weeklycal/7
print(f'Daily: {daily} euros')
print(f'Weekly: {weeklycal} euros')