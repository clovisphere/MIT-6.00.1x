
# variable 's' is defined/declared and used for testing purposes only.
# while submitting for review (on Edx), it'd be removed.
s = ''

# solution starts here
valid_vowels = ['a', 'e', 'i', 'o', 'u'] 
print('Number of vowels: {}'.format(len([v for v in s if v in valid_vowels])))
