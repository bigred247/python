## this function will only list AMIs currently in use and print the output
## it will not delete any AMIs!

import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')
ec2_client = boto3.client('ec2')

# Identify AMIs which are being used currently
response = ec2_client.describe_instances()
used_amis = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

#Remove duplicate AMI IDs
def remove_duplicates(amis):
    unique_amis = []
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis
unique_amis = remove_duplicates(used_amis)

print("\n" * 1)
print("The below AMIs are currently IN-USE in this AWS account so do NOT delete:")
print(unique_amis)
print("\n" * 1)