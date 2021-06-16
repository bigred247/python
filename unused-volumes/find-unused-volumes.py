import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')

#Clients
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

#Variables
volumes = ec2_client.describe_volumes()
size = 0
iops = 0
sns_arn = 'arn:aws:sns:eu-west-2:500441578972:alerts'

#Function - find and list volumes that are not attached
unused_volumes = []
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_volumes.append(volume['VolumeId'])
        size = size + volume['Size']
        iops = iops + volume['Iops']
        #print(volume)
        #print("\n" * 5)

#Email body
email_body = "##### Unused Volumes ##### \n"
for vol in unused_volumes:
    email_body = email_body + "VolumeId = {} \n".format(vol)

email_body = email_body + "\n\nTotal Unused Volume Size = {}".format(size)

email_body = email_body + "\n\nTotal IOPS = {}".format(iops)

#Send Email
sns_client.publish(
    TopicArn='arn:aws:sns:eu-west-2:500441578972:alerts',
    Subject='Unused Volumes',
    Message=email_body 
)

print(email_body)