`pop()` 
is an inbuilt function in Python that removes and returns last value from the list or the given index value.

`remove` 
The remove() method removes the first matching element (which is passed as an argument) from the list.

`txt.index("welcome")` 
The index() method finds the first occurrence of the specified value `welcome`.

`find`
The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found
fruits.

`count`
("cherry")` fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
Return the number of times the value "cherry" appears in the fruits list: so 1 in this case

`!=`
This means NOT EQUAL to. So 55 != 99 would return `True`
e.g. `print("mouse" != "mouse")` would return `False` because mouse is equal to mouse.

`elif`
The first elif that is True will be executed when multiple elif statements are True.

`print("lion" == "cat" or 99 != 88)`
What does the above code print to the console? True is printed. "lion" == "cat" evaluates to False and 99 != 88 evaluates to True. False or True evaluates to True for the final result.

`if 1:`  
    `print("1 is truthy!")`  
`else:`  
    `print("???")`  
What does the above code print to the console? "1 is truthy!" is printed.' 1 does not equal True, but it's considered True in a boolean context. Values that are considered True in a boolean context are called "truthy" and values that are considered False in a boolean context are called "falsy".

`intersection`
The intersection() method returns a set that contains the similarity between two or more sets. Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

`difference`
The difference() method returns a set that contains the difference between two sets. Meaning: The returned set contains items that exist only in the first set, and not in both sets.

`reduce`
collates the numbers together e.g [2, 2, 13, 15] = 32 and [30, 45] = 75. There is more

`round`
This rounds off a number to the nearest whole number for example `round(45.8)` would result in 46.

`range`
In a range the first number is included. Per below, 3 is included but 10 is not. And the 2 is the incremental value. So print will result in 3, 5, 7, 9.  
>x = range(3, 10, 2)  
for n in x:  
print(n)

`numbers`
binary = 2
octal (0o)= 8
decimal = 10
hexadecimal = 16

`method items()`
Returns the tuples

`//` (floor division)
floor division divides the value and returns the highest possible `floored value` (similar to rounded but is rounded to the lowest number) 
e.g. 3 // 3 = 1  
but 5 // 3 also equals 1  
The number is floored (sort of rounded down to the nearest lowest valued).
So 1.5 will be floored to 1  
and `-1.5 will be floored down to -2.0` because -2.0 is a lower (floored) value than 1.5. And 1.5 is not a round number!  
print(-6 // -4) the answer is `1`  
print(-6 //-3) the answer is `2`  
BUT for `negative` numbers e.g. print(-6 // 4) the answer is `-2.0`.  
This is because -6 / 4 = `-1.5`. Rounded (floored) down to the nearest low value = -2.0  
This `also` applies to 6 / -4 which = `-1.5`. Floored down this is also = -2.0  

`%` (what remains behind)  
5 % 2 = 1   # 1 is left behind
BUT 3 % 4 = `3` and 1 % 2 will = `1` because neither are divisble so do not leave a `remainder` as whole numbers so the left value remains in tact.

`input()`  
In Python, we use input() function to take input from the user. Whatever you enter as input, the input function converts it into a string. If you enter an integer value still input() function convert it into a string.  

`function`
- a python function must be placed before the first invocation
- if a list is passed into a functions argument and modified inside the function, it will affect the argument!  
- it is legal to have a variable named the same as a functions parameter

`is`
must be idential

>tech = ['panda', 'bear']  
tech2 = ['panda', 'bear']  
tech_copy = tech  
print(tech is tech_copy)  
print(tech is tech2)  

= True
  False

`^`  
XOR	Sets each bit to 1 if only one of two bits is 1.
a=0  
b=1  
print(a^b)  
= 1  

BUT  

a=1  
b=1  
print(a^b)  
= 0  

a=1  
b=1  
print(a^b)  
= 0  

`2**2**3`  
x to the power of y  
so for an equation like `2**2**3`  
you do the right bind first = 2 to power 3 = 8  
then you do left bind which is 2 to power of 2 which = 4  
so you then have `2**8` which equals 256  

`input`
Input1 = int(input("Enter the first number: ")) # Enter 23
Input2 = int(input("Enter the second number: ")) # Enter 22
print(Input1 + Input2)
= 45 #treated like a int

Input1 = input("Enter the first number: ") # Enter 23
Input2 = input("Enter the second number: ") # Enter 22
print(Input1 + Input2)
= 2322 #treated like a string

num1 = input())# Enter 2
num2 = int(input()) # Enter 3
print(num1*num2)
= 222 (three lots of 2s)

num1 = int(input())# Enter 2
num2 = int(input()) # Enter 3
print(num1*num2)
= 6

`not`
In Python, empty sequences such as (), [], '' and {} all evaluate to False, as well as the `interger 0`.
Since a None value is falsy, it returns true

print(bool(0))  = False
print(bool(7))  = True
print(bool('')) = False

print(not(bool(0)))  = False
print(not(bool(7)))  = True
print(not(bool(''))) = False

`none`
- is a keyword
- can be assigned to a var
- can be used to compare a var
