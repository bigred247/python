from enum import unique
import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')
ec2_client = boto3.client('ec2')

# 1. Identify AMIs which are being used currently by instances
being_used = ec2_client.describe_instances()
used_amis = []
for reservation in being_used['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

# 2. Remove duplicate AMI IDs
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

# 3. Get custom AMIs from account owned by self
custom_images = ec2_client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available',
            ]
        },
    ],
    Owners= ['self']
)
custom_amis_list = []
for images in custom_images['Images']:
    custom_amis_list.append(images['ImageId'])

print("\n" * 1)
print("The AMIs below are all the 'Custom' created AMIs' that exist in this AWS account.")
print(custom_amis_list)
print("\n" * 1)

# 4. Deregister AMIs not being used

for custom_ami in custom_amis_list:
    if custom_ami not in used_amis:
        print("deregistering ami {}".format(custom_ami))
        deregister_amis = ec2_client.deregister_image(ImageId=images['ImageId'], DryRun=True)