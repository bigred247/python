import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print('Instance id is {} and Instance Type is {}'.format(instance.instance_id, instance.instance_type))