import boto3
rds = boto3.setup_default_session(profile_name='ifdev')
client = boto3.client('rds')

response = client.describe_db_instances()

for instance in response['DBInstances']:
    print("Instance {} is still alive".format(instance['DBInstanceIdentifier']))
