import requests
response = requests.get('https://google.com/')
print("Received response code", response.status_code)
if response:
  print('Request is successful.')
else:
  print('Request returned an error.')