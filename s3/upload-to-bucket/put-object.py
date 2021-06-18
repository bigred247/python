# Puts file object in s3 bucket
 
import boto3
client = boto3.client('s3')

# Variables
bucket_name = 'lambda-test-create-bucket'
aws_account = '500441578972'
file_reader = open('test_file.py').read() #do not need to specify

# Function
put_file = client.put_object(
    ACL='public-read', 
    Body=file_reader,  #do not need to specify
    Bucket=bucket_name,
    Key='test_file.py',
    ServerSideEncryption='AES256',
    StorageClass='REDUCED_REDUNDANCY',
    Tagging='python-test-tag',
    ExpectedBucketOwner=aws_account
)

# Output to screen
print(put_file)