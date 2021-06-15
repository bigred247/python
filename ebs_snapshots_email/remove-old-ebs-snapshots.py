from datetime import datetime, timedelta, timezone

import boto3
boto3.setup_default_session(profile_name='eng', region_name='eu-west-2')
ec2 = boto3.resource('ec2')

# List(ec2.Snapshot)
snapshots = ec2.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=90)
    if delete_time > start_time:
        snapshot.delete()
        print('Snapshot with Id = {} is deleted '.format(snapshot.snapshot_id))
