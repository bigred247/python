#example 1
print_return = print('Hello world')
print(print_return)

#example 2
x = None
if x:
    print("None is True")
elif x is False:
    print ("None is False")
else:
    print("None is not True, or False, None is just None") 

# example 3
x = None
if x is None:
    print('yes')
if x == None:
    print('it does')

# example 4
def greet():
    print('hello!')

x = greet()
print(x)