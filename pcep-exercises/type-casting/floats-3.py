a = int(input('First number: '))
b = int(input('Second number: '))
 
a = a % b # 13 & 3 = 3 goes in 4 times totalling 12 - leaving 1
b = b % a # 3 % 1 = 0 because 1 goes into 3 three times leaving 0 balance
 
print(a, b)

#First number: 13
#Second number: 3
#Answer = 1 0
# First, a = 13 % 3, which is 1. So a = 1 after this opeartion. Now, b = 3 % 1, which is 0. So b = 0. 