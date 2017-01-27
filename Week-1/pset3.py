
# variable 's' is defined/declared and used for testing purposes only.
# while submitting for review (on Edx), it'd be removed.
s = ''

# solution starts here
words = []  # will hold valid sub-string(s) from given word.
count = 0

for letter in s:
    sub_string = s[(count + 1):]
    current_letter = temp = letter
    for i in sub_string:
        if current_letter <= i:
            temp += i
            current_letter = i
        else:
            break
    words.append(temp)
    count += 1

longest = words[0]  # assumes the longest sub-string is the first index.

for word in words:
    if len(longest) < len(word):
        longest = word

print('Longest substring in alphabetical order is: {}'.format(longest))
