# example 1
def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)# note there are 2 print statements!
print_letter_count('How many letters a are here?')# note there are 2 print statements!

# example 2
def print_letter_count(text='dunnomate', letter='n'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count()