# to use with lambda
import boto3
ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')

def lambda_handler(event, context):
    response = ec2_client.describe_addresses()
    unused_eips = []
    for address in response['Addresses']:
        if 'InstanceId' not in address:
            unused_eips.append(address['PublicIp'])

    print(unused_eips)