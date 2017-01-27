
# variable 's' is defined/declared and used for testing purposes only.
# while submitting for review (on Edx), it'd be removed.
s = ''

# solution starts here
str_to_find = 'bob'
occurrences = start = 0

while True:
    start = s.lower().find(str_to_find, start) + 1
    if start > 0:
        occurrences += 1
    else:
        break

print('Number of times {0} occurs is: {1}'.format(str_to_find, occurrences))