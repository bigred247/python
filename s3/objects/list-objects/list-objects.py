# List all objects in an s3 bucket
 
import boto3
client = boto3.client('s3')

# Variables
bucket_name = 'lambda-test-create-bucket'
aws_account = '500441578972'

# Functions
response = client.list_objects(
    Bucket=bucket_name,
    ExpectedBucketOwner=aws_account
)

for content in response['Contents']:
    #print(content['Size'], content['StorageClass'])
    print(content['Key'])