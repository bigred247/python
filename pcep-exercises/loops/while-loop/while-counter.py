counter = 1
while counter < 11:
  print(counter)

#What does the above code do?
# it prints an INFINITE loop of number 1s!!!
# You will have to ctrl + esc to break from it.,



counter = 1
while counter < 11:
    print(counter)
    counter += 1         #the above is missing this 
print('Finished!')

#output below
'''
1
2
3
4
5
6
7
8
9
10
Finished!
'''