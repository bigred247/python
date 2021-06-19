
# unary operators
-2
+5

# binary operators
# 1. **
# 2. * / // %
# 3. + -
2 ** 3 ** 2 # = 2 ** 9 = 512


# bitwise operators
& | ^ ~ << >>

x = 0
y = 1
a = x ^ y # = 1 # means "exlusive or" # as long as one of the bits is 1, you will see a result of 1 
b = x | y # = 1 # the bar means "or" # as long as one of the bits is 1, you will see a result of 1 
c = x & y # = 0 # means "and" # if both values are 1 then you will see the 1 bit. If one or both are 0 then you see 0
print(a + b + c)
= 2
# That's because: a = 0 ^ 1 = 1, b = 0 | 1 = 1, c = 0 & 1 = 0. Then: a + b + c = 1 + 1 + 0 = 2



What will be the output of the following snippet?
print(18 >> 1)
= 9
The right-shift operator used with the number one (>> 1) on an integer divides the integer's value by two.



What is the result of the following expression in Python?
1 // 2 * 3
= 0 #python will NOT show an error
= First, Python will evaluate 1 // 2, which is 0. Then, 0 * 3 = 0.


# float accuracy - is not exact. See example below.
print(0.1 + 0.1 + 0.1)
= 0.30000000000000004


age = int(input('What is your age?'))
average = float(input('Your average weight?'))


count=len('How many characters are here?')
print(count)



print('is this', 'a dream', sep='=', end='? ')
print('I do not think', 'it is', sep='#')


= is this=a dream? I do not think#it is



2 + 3 * 5 # multiplication goes first



height = float(input('Your height in cm?'))
height_feet = height * 0.33
msg = 'You are ' + str(height_feet) + ' ft tall'


# standard divsion
What is the result of the following division in Python?

1 / 1

= 1.0 # standard division always shows a FLOAT