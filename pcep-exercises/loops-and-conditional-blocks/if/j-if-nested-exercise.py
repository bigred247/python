faulty = input('Has the item broken down on its own? y/n ')
days = int(input('How many days ago have you purchased your item? '))
been_used = input('Have you used the item at all? y/n ')

if faulty == 'y' or days <= 10 and been_used =='n':
    print('You can get a refund')
else:
    print('You cannot get a refund but we may consider exchanging the item per our T&Cs')

#if faulty = y >> then you should be entitled to a refund regardless

# below is the instructors answer
""" purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.') """