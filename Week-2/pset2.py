# The below variables are used for testing purposes only.
# while submitting for review (on Edx), they'd be removed.
# Note: The naming convention may differ.
balance = 3926
annual_interest_rate = 0.2

# solution starts here
minimum = 0
months = 12

while True:
	monthly_interest_rate = annual_interest_rate/months
	temp = balance
	
	for month in range(months):
		temp = (temp - minimum) + (monthly_interest_rate * (temp - minimum))
	
	if temp > 0:
		minimum += 10
	else:
		break
print('Lowest Payment: {}'.format(minimum))