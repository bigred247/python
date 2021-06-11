import boto3
session = boto3.session.Session(profile_name='prod')
#client = session.client('ec2')
#boto3.setup_default_session(profile_name='mgmt')
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print('Instance id is {} and Instance Type is {}'.format(instance.instance_id, instance.instance_type))