import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')
ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

backup_filter = [
    {
    'Name': 'tag:Backup',
    'Values': ['true']
    }
]
snapshot_ids = []

#Looping through the ec2 instance list (ec2.Instance)
for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn='arn:aws:sns:eu-west-2:500441578972:snapshots',
    Subject='EBS Snapshots for web server',
    Message= str(snapshot_ids) 
)
