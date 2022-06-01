import csv
with open('/home/fraz/my_repos/github/Python/csv/list_of_cars.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))