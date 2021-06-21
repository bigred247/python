list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

#output
# Original: [-5, 2, 3] 
# New: [1, 2]