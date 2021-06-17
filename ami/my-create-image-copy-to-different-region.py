import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')

##########################
## Part-1 Create Images ##
##########################

source_region = 'eu-west-2'
ec2 = boto3.resource('ec2', region_name=source_region)


instances = ec2.instances.filter(InstanceIds=['i-0ee1794ccfc47ea57'])

image_ids = []

for instance in instances:
    image = instance.create_image(Name='Demo Boto - '+instance.id, Description='Demo Boto'+instance.id)
    image_ids.append(image.id)

print("Images to be copied {} ".format(image_ids))


#############################################
## Part-2 Wait For Images to be available  ##
#############################################
# Get waiter for image_available

client = boto3.client('ec2', region_name=source_region)
waiter = client.get_waiter('image_available')

# Wait for Images to be ready
waiter.wait(Filters=[{
    'Name': 'image-id',
    'Values': image_ids
}])

##########################################
## Part-3 Copy Images to other regions  ##
##########################################

# Copy Images to the region, us-east-1

destination_region = 'us-east-1'
client = boto3.client('ec2', region_name=destination_region)
for image_id in image_ids:
    client.copy_image(Name='Boto3 Copy'+image_id, SourceImageId=image_id, SourceRegion='eu-west-2')



