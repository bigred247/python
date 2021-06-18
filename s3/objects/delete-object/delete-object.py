# Delete a specific file in an s3 bucket
 
import boto3
client = boto3.client('s3')

# Variables
bucket_name = 'lambda-test-create-bucket'
aws_account = '500441578972'
file_name = 'json/instructions.md'

# Function
delete_file = client.delete_object(
    Bucket=bucket_name,
    Key=file_name,
    ExpectedBucketOwner=aws_account
)

# Output to screen
print(delete_file)