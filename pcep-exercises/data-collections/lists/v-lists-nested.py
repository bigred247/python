#nested list
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

#method 1
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)

#Answer = 
Element: ['A1', 'A2', 'A3']
Element: ['B1', 'B2', 'B3']

#method 2
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)

#Answer =
Element: A1
Element: A2
Element: A3
Element: B1
Element: B2
Element: B3


#method 4
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

#answer
A1 A2 A3 
B1 B2 B3 

##medthod 5

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

#answer = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
