# The below variables are used for testing purposes only.
# while submitting for review (on Edx), they'd be removed.
# Note: The naming convention may differ.
balance = 4773
annual_interest_rate = 0.2

# solution starts here
minimum_fixed_payment = 0
number_of_month = 12

while True:
	monthly_interest_rate = annual_interest_rate/number_of_month
	temp = balance
	
	for month in range(number_of_month):
		temp = (temp - minimum_fixed_payment) + \
		 (monthly_interest_rate * (temp - minimum_fixed_payment))
	
	if temp > 0:
		minimum_fixed_payment += 10
	else:
		break
print('Lowest Payment: {}'.format(minimum_fixed_payment))