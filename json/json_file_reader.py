import json

# Opening JSON file
f = open('/home/fraz/my_repos/github/Python/json/data.json')

# returns JSON object as a dictionary
# both statements below work - choose either/or:

#data=json.load(f)
data=json.loads(f.read())

# extracts all data
for i in data['emp_details']:
    print(i)

# extracts just age
for b in data['emp_details']:
    print(b['age'])

# Closing file
f.close()

