answer_a = input('Do you like travelling? y/n: ')
if answer_a == 'y':
    answer_b = input('And do you like Asia? y/n: ')
    if answer_b == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')

#There can only be one else statement in a single if instruction. 
#If two, Python will show an error.
# Here we a second else statement but it is a sub statement of the first - see indent 