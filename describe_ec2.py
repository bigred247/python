import boto3
client = boto3.client('ec2')
response = client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {}".format(instance['InstanceId']))
        print("InstanceType is {}".format(instance['InstanceType']))
        print("InstanceType is {}".format(instance['Tags']))