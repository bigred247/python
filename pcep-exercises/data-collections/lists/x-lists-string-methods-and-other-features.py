String methods can be found here: https://www.w3schools.com/python/python_ref_string.asp
 
#prints 6th letter

fav_band = 'Green Day'
print(fav_band[6])

#Answer = D


#print CAPITAL letters
text = 'please capitlise me'
text_cap = text.upper()
print(text_cap)

# = PLEASE CAPITLISE ME


# erorrs if not number
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')

#Please provide a number: ala
#Sorry, ala is not a number!