import boto3
client=boto3.client("iam")
response=client.get_credential_report()
data=response["Content"]
data=data.decode("utf-8")
data=data.split("\n")
for user in data[1:]:
    print(user.split(",")[0],user.split(",")[2])