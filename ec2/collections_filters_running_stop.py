import boto3
ec2 = boto3.resource('ec2')
ec2.instances.filter(Filters=[
    {
        'Name': 'instance-state-name',
        'Values': ['stopped'] #use running here
    }
]).start() #can use stop here