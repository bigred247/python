import boto3
client = boto3.client("iam")
response = client.list_roles()
#print(response)
print(response.values())
#above prints values and not keys 