grades = {
    'Jason': 'A+',
    'Peter': 'B-',
    'Mark': 'D'
}

print('original exam takers: ', grades)

#adds John and Abdul to the dictionary print output
grades['John'] = 'A-'
grades['Abdul'] = 'C'
print('with new exam takers: ', grades)

#only prints Abdul's grade
print(grades['Abdul'])
