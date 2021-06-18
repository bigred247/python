import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.delete_item(
    Key={
            'emp_id': '123'
         }
)