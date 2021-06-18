# Create S3 bucket
import boto3
client = boto3.client('s3')

# Variables
bucket_name = 'lambda-test-create-bucket'

# Function
create_s3 = client.create_bucket(
    ACL='private',
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'
    }
)

# Output to screen
print(create_s3)