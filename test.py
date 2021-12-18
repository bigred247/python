import boto3
client=boto3.client("iam")
response=client.get_credential_report()
data=response["Content"]
data=data.decode("utf-8")
print(data)
print(type(data))