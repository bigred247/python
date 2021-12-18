import boto3
client = boto3.client("iam")
response = client.list_policies()
#print(response.keys())
policies=response["Policies"]
#above returns just the results for the "Policies" Key
#print(policies)
for policy in policies:
    #below prints the policy name and arn from the policies dictionary key
    print(policy["PolicyName"], policy["Arn"])
