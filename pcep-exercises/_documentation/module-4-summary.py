Exam block #4: Data Collections – Lists, Tuples, and Dictionaries (23%)
Objectives covered by the block (7 exam items)

simple lists: constructing vectors, indexing and slicing, the len() function
lists in detail: indexing, slicing, basic methods (append(), insert(), index()) and functions (len(), sorted(), etc.), del instruction, iterating lists with the for loop, initializing, in and not in operators, list comprehension, copying and cloning
lists in lists: matrices and cubes
tuples: indexing, slicing, building, immutability
tuples vs. lists: similarities and differences, lists inside tuples and tuples inside lists
dictionaries: building, indexing, adding and removing keys, iterating through dictionaries as well as their keys and values, checking key existence, keys(), items() and values() methods
strings in detail: escaping using the \ character, quotes and apostrophes inside strings, multi-line strings, basic string functions.


# Mutable vs Immutable
Strings = immutable - 'Strings are immutable in Python and you can\'t change individual characters inside them'
Lists = are mutable!!! and can be changed!!
Tuple = immutable - can NOT change using append or del (you can edit a list inside a tuple - see tuple folder for example)

# Tuple types
numbers = 1, 2, 3
Elements separated by commas without square brackets create a tuple in Python.



#Dictionary inc LEN
grades = {
    'Jason': 'A+',
    'Peter': 'B-',
    'Matthew': 'F',
    'Mark': 'D',
    'Luke': 'C',
    'John': 'B'
}

#print('the number of students that passed their exams are: ', len(grades))
print(len(grades), 'students have passed their mid-term exams')


top_city = 'New York City'
top_cities = []
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0]
top_cities[-5]
top_cities[0:3]

# Standard variables

city_1 = 'New York City'
city_2 = 'Los Angeles'
city_3 = 'Chicago'
city_4 = 'Houston'
city_5 = 'Phoenix'

# empty variable
empty_list = []


# multi variables
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)

answer=
['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']


top_cities[0]
= 'New York City'

top_cities[4]
= 'Phoenix'

top_cities[-1]
= 'Phoenix'

top_cities[-5]
= 'New York City'

top_cities[0:2]
= ['New York City', 'Los Angeles'] # inc 0 and 1 but NOT 2

top_cities[:3] # inc 0, 1 and 3

top_cities[:] # inc all