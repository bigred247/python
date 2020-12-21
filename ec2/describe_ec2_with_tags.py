import boto3
client = boto3.client('ec2')
response = client.describe_instances(Filters=[{
    'Name': 'tag:eks:nodegroup-name',
    'Values': ['engineering-eks-node-group-01-moved-cougar']
}])

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {}".format(instance['InstanceId']))
        print("InstanceType is {}".format(instance['InstanceType']))
