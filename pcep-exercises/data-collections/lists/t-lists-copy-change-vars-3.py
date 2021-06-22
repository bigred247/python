list_original = [1, 2, 3]
list_new = list_original[:2] 
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

#the [:2] selects the first two values e.g. 1,2. If it was [0:2] it will only take the 0 and 1 postional values and not the 2. So would result in 1,2 again

#output
# Original: [-5, 2, 3] 
# New: [1, 2]