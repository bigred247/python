list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5 #this replaces the 1 (which is [0]) with a -5 value in the original list
print('Original:', list_original, '\nNew:', list_new)

#output
# Original: [-5, 2, 3] 
# New: [1, 2, 3]