import json

# some JSON:
user_1 =  '{ "name":"John", "age":30, "city":"New York"}'

# parse user_1:
y = json.loads(user_1)

# the result is a Python dictionary:
print(y["name"], y["age"])