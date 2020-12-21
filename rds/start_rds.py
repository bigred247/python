import boto3
rds = boto3.setup_default_session(profile_name='ifdev')
client = boto3.client('rds')

response = client.start_db_instance(
    DBInstanceIdentifier='ifdev-mysql-rds'
)
