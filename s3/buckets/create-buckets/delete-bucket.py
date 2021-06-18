# Delete S3 bucket
import boto3
client = boto3.client('s3')

# Variables
bucket_name = 'lambda-test-create-bucket'
aws_account = '500441578972'

# Function
delete_s3 = client.delete_bucket(
    Bucket=bucket_name,
    ExpectedBucketOwner=aws_account
)

# Output to screen
print(delete_s3)