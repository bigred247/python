import boto3
client = boto3.client('ec2')
response = client.terminate_instances(InstanceIds=['i-0be4c400d96ef5da7'])

for instance in response['TerminatingInstances']:
    print("Instance {} has been terminated successfully".format(instance['InstanceId']))