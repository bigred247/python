Exam block #3: Control Flow – loops and conditional blocks (20%)
Objectives covered by the block (6 exam items)

conditional statements: if, if-else, if-elif, if-elif-else
multiple conditional statements
the pass instruction
building loops: while, for, range(), in
iterating through sequences
expanding loops: while-else, for-else
nesting loops and conditional statements
controlling loop execution: break, continue



What will be the value of x after this code is executed?

x = 1
x = x == x
print(x)
= True


#  available logical operators
#
#  <  less than
#  >  greater than
#  <= less than or equal
#  >= greater than or equal
#  == equals
#  != not equals


if True:
    print('Condition met')
#returns = Condition met

if False:
    print('Condition met')
#returns =

if 2 == 2:
    print('true')
#returns = true

if 1 == 2:
    print('true')
#returns = 

if 2 == 2.0:
    print('true')
#returns = true


# Joining Multiple Conditions - in preferential order
See below operators for joining:

# not
# and
# or

Please note the order of perefernce is 'not'. followed by 'and' and then finally 'or'


What will be the output of the following snippet?

a = 5
b = 1
c = a > b or b < a and a == 1
print(c)

answer = True

# Explanation
a > b or b < a and a == 1 means (a > b) or (b < a and a == 1) which means (True) or (False and False) which means (True) or (False) which means True

# else 
There can only be one else statement in a single if instruction. 
If two, Python will show an error.