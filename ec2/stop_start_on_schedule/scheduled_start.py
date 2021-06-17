import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filter = [
           {
            'Name' : 'tag:Scheduled',
            'Values' : ['true']
           }
       ]

    instances = ec2.instances.filter(Filters=filter)
    for instance in instances:
        instance.start()
    
    return 'Success'