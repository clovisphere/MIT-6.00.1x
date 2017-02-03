# The below variables are used for testing purposes only.
# while submitting for review (on Edx), they'd be removed.
# Note: The naming convention may differ.
balance = 5000
annual_interest_rate = 0.18
monthly_payment_rate = 0.02

# solution starts here
number_of_month = 12

for month in range(number_of_month):
	balance = (balance - (balance * monthly_payment_rate)) \
		+ (annual_interest_rate/number_of_month) \
		* (balance - (balance * monthly_payment_rate))
	
print('Remaining balance: {:.2f}'.format(balance))