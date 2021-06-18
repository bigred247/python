# Select Specific rows, columns from CSV filed stored in S3

import boto3

client = boto3.client('s3')

response = client.select_object_content(
    Bucket='lambda-test-create-bucket',
    Key='json/employees.csv',
    Expression='Select s.name, s.email from S3Object s',
    ExpressionType='SQL',
    InputSerialization={'CSV': {'FileHeaderInfo': 'USE'}},
    OutputSerialization={'JSON': {}}
)

# Loop through Payload object in response syntax
for event in response['Payload']:
    if 'Records' in event:
        print(event['Records']['Payload'].decode())
