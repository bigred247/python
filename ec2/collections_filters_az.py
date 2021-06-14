import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')
ec2 = boto3.resource('ec2')
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['eu-west-2a']
    }
]):
    print('Instance id is {} and Instance Type is {}'.format(instance.instance_id, instance.instance_type))