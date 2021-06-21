birth_year = int(input('Which year were you born in?'))
user_country = input('Which country are you travelling from?')
if birth_year >= 1978 and birth_year <= 2010 \
and not user_country == 'France':
    print('Congratulations. You qualify for the programme')
else:
    print('On your bike pal!')