import boto3

client = boto3.client('autoscaling')

response = client.resume_processes(
    AutoScalingGroupName='my-auto-scaling-group',
    ScalingProcesses=[
        'Launch',
        'Terminate',
        'AddToLoadBalancer',
        'AlarmNotification',
        'AZRebalance',
        'HealthCheck',
        'InstanceRefresh',
        'ReplaceUnhealthy',
        'ScheduledActions',
    ],
)

print("all asg processess have been RESUMED")