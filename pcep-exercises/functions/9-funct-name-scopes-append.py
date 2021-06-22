def show_truth():
    mysterious_var.append('New Surprise!')
    print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)

'''
output = 

['Surprise!']
['Surprise!', 'New Surprise!']
['Surprise!', 'New Surprise!']

'''