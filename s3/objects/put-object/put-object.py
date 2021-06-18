# Puts file object in s3 bucket
 
import boto3
client = boto3.client('s3')

# Variables
bucket_name = 'lambda-test-create-bucket'
aws_account = '500441578972'
file_name = 'employees.csv'
key = 'json/employees.csv'
file_reader = open(file_name).read() #do not need to specify

# Function
put_file = client.put_object(
    ACL='public-read', 
    Body=file_reader,  #do not need to specify
    Bucket=bucket_name,
    Key=key,
    ServerSideEncryption='AES256',
    StorageClass='STANDARD',
    Tagging='uploaded-by-python',
    ExpectedBucketOwner=aws_account
)

# Output to screen
print(put_file)