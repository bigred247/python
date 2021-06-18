# You can run this directly from vscode
# lambda handler is commented out and there are no indents
# use file 'ses-alert-lambda.zip' to deploy function to lambda

import boto3
ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

response = ec2_client.describe_addresses()
unused_eips = []
for address in response['Addresses']:
    if 'InstanceId' not in address:
        unused_eips.append(address['PublicIp'])

print(unused_eips)
    