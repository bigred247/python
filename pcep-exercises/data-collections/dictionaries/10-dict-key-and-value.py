grades = {
    'Jason': 'A+++',
    'Peter': 'B-',
    'Matthew': 'F',
    'Mark': 'D',
    'Luke': 'C',
    'John': 'B'
}

for name, grade in grades.items():
    print(name, 'was graded', grade)
    #print(name,grade, sep=', ') #ready for csv format