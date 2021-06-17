import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')
client = boto3.client('ec2')
response = client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {}".format(instance['InstanceId']))
        print("InstanceType is {}".format(instance['InstanceType']))
        print("InstanceType is {}".format(instance['Tags']))
        print("\n" * 3) #creates 3 line spaces between output