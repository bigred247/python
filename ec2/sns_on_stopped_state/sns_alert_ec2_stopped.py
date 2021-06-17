import boto3
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:eu-west-2:500441578972:alerts'
    message = 'Prod ec2 WEB server has stopped. Please raise a ticket and investigate'
    sns_client.publish(TopicArn=topic_arn,Message=message)