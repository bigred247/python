# display all EIPs in AWS acct

import boto3
ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

response = ec2_client.describe_addresses()
for address in response['Addresses']:
    print(address['PublicIp'], address['AllocationId'])