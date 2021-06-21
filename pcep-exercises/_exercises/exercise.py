while True:
    year = int(input('When was Python 1.0 release? '))
    if year < 1994:
        print('It was later than that. Try again.')
    elif year > 1994:
        print('It was earlier than that. Try again.')
    else:
        print('Correct.')
        break