import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
resp = table.get_item(
    Key={
        'emp_id': '2'
    }
)

print(resp['Item'])

table.delete_item(
    Key={
        'emp_id': '2'
    }
)