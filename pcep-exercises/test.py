                                        [LEGEND]
when using standard numbers      [ 1,  2,  3,  4,  5]
when using negative "-" numbers  [-5, -4, -3, -2, -1]
So -1 maps to 5, -2 maps to 4 and so on

list_original = [1, 2, 3, 4, 5]  
print(list_original[-5:-1])
#  = [1, 2, 3, 4]
# [-5:-1] number on right "-1" is the right most and is refers to "5" in the var list_original. 
# The right number is always negated. So -1 means negate "5" in the list_original
# The left most number "-5" refers to 1 in the var list_original and is included in the output  

list_original = [1, 2, 3, 4, 5]
print(list_original[-4:-1])
#  =[2, 3, 4]

list_original = [1, 2, 3, 4, 5]
print(list_original[-3:-1])
#  =[3, 4]

list_original = [1, 2, 3, 4, 5]
print(list_original[-2:-1])
#  =[4]


######
#Reversing values results in [] for all
######

list_original = [1, 2, 3, 4, 5]
print(list_original[-1:-5])
#  = []

list_original = [1, 2, 3, 4, 5]
print(list_original[-1:-4])
#  = []

list_original = [1, 2, 3, 4, 5]
print(list_original[-1:-3])
#  = []

list_original = [1, 2, 3, 4, 5]
print(list_original[-1:-2])
#  = []

list_original = [1, 2, 3, 4, 5]
print(list_original[-1:-1])
#  = []