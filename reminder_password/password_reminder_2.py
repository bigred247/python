import boto3
boto3.setup_default_session(profile_name='devops-lab', region_name='eu-west-2')
client=boto3.client("iam")
response=client.get_user()
data=response["User"]
for user in data:
    for name in user['UserName']:
      print(name)