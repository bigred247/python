# Exam block #1: Basic Concepts (17%)
Objectives covered by the block (5 exam items)

# literals: Boolean, integer, floating-point numbers, scientific notation, strings
sample_boolean = True #or False
sample_integer = 4
sample_float = 4.0
sample_scientific = 4.23e27
sample_string = 'Hello!'

# scientific notation
3e4 = 3E4 = 3 * 10000 = 30000
3e-4 = 3E-4 = 3 * 1/10000 = 0.0003
print(0.000000000000000000000000003)

# underscores in numbers - cannot use commas ,
12000300
12_000_300

# all-line comment
age = 25 # mid-line comment

# the print() function
print('Hello!', 'Nice to see you.')

# the input() function
input('What\'s your name?') # input() always returns a string value.

# numeral systems (binary, octal, decimal, hexadecimal)
sample_octal = 0o17
sample_hexadecimal = 0x123
sample_decimal = 28

# octal numbers
# start with 0O or 0o
print(0o123)

# hexadecimal numbers
# start with 0X or 0x
print(0x123)

# numeric operators: ** * / % // + –
# exponentation
2 ** 10 # 2 to the power of 10
= 1024

2 ** 2 ** 3
= 256 # when it comes to this operator, python starts from the right - others start from the left 


# multipication
3 * 5
= 15

# three kinds of division
print(13 / 2) #Standard division always returns an float.
print(13 // 2) #Integer division always produces the closest integer rounded down.
print(13 % 2) #


# addition and subtraction
print(2 + 7)
print(3 - 8)

# string addition
'one' + 'two'

# string multiplication
'one' * 3

# assignments and shortcut operators
age = 25
age = age + 5
age += 5
age *= 2

# Variables
Cannot start with a number!!! Only letters and underscore _ are acceptable