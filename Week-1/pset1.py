
# variable 's' is defined/declared and used for testing purposes only.
# while submitting for review (on Edx), it'd be removed.
s = ''

# solution starts here
valid_vowel = ['a', 'e', 'i', 'o', 'u']
number_of_vowel = 0

for letter in s:
    if letter.lower() in valid_vowel:
        number_of_vowel += 1

print('Number of vowels: {}'.format(number_of_vowel))