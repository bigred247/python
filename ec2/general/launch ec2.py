import boto3
client = boto3.client('ec2')
output = client.run_instances(ImageId='ami-08b993f76f42c3e2f',
                     InstanceType='t2.micro',
                     MaxCount=1,
                     MinCount=1,
                     SubnetId='subnet-06fc5da3fae3f819e')

for instance in output['Instances']:
    print(instance['InstanceId'])
    print(instance['LaunchTime'])
    print(instance['PrivateDnsName'])