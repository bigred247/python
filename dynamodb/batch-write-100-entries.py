# this script creates 100 users with a prefix name of 'Name-'
# and role of 'Waiter-'

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

with table.batch_writer() as batch:
    for x in range(100):
        batch.put_item(
            Item={
                  'emp_id': str(x),
                  'name': 'Name-{}'.format(x),
                  'role': 'Waiter-{}'.format(x),
                  }
    )
    # You can also delete_items in a batch.
    #batch.delete_item(Key={'HashKey': 'SomeHashKey'})