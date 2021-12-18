import boto3
#boto3.setup_default_session(profile_name='devops-lab', region_name='eu-west-2')
client=boto3.client("iam")
response=client.list_users()
#print(response["Users"])
#print(response.keys())
#the above will print all keys inside the dictionary for list_users
users=response["Users"]
for user in users:
  print(user["UserName"], user["UserId"])