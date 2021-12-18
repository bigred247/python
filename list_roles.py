import boto3
client = boto3.client("iam")
response = client.list_roles()
#print(response)
#print(response.keys())
#print(response["Roles"])
roles = response["Roles"]
for role in roles:
    print(role["RoleName"], role["CreateDate"])
