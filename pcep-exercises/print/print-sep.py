first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep='-', end='=')
print('\n')
#the sep value of "-" replaces the spaces between the 'is', 'first_name' and 'welcome' words with a hyphen "-" instead of the default space 

#example
first_name = 'John'
print(sep=' - ', 'Your first name is', first_name, 'Welcome!')
#in this example, the keyword sep argument appears before positional arguments, which is why Python will show an error