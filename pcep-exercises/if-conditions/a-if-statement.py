user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
elif user_age < 20:
    print('You are too young. You must be over 20 years of age and above')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')



There can only be one else statement in a single if instruction. 
If two, Python will show an error.

# a conditional statement must have 
# at least 1 x if
# as many elif statements as required
# and 0 or 1 x else statements