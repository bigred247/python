grades = {
    'Jason': 'A+++',
    'Peter': 'B-',
    'Matthew': 'F',
    'Mark': 'D',
    'Luke': 'C',
    'John': 'B'
}

'''
# method 1 - prints dictionary key 
for el in grades: #prints "key" value in list format e.g. the names in dictionary in this scenario
    print(el)     #the 'el' control variable can be replaced with any word here
'''

# method 2 - prints dictionary key
for el in grades.keys():
    print(el)