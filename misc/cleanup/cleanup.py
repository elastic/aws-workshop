import boto3

# Set the AWS region
region_name = "us-west-2"

# Initialize the clients
ec2 = boto3.client('ec2', region_name=region_name)
cloudwatch = boto3.client('logs', region_name=region_name)
cloudtrail = boto3.client('cloudtrail', region_name=region_name)
sqs = boto3.client('sqs', region_name=region_name)

# List of security groups to delete
security_group_names = ["elastic-agent"]

# Delete specified security groups
try:
    security_groups = ec2.describe_security_groups()['SecurityGroups']
    for security_group in security_groups:
        if security_group['GroupName'] in security_group_names:
            ec2.delete_security_group(GroupId=security_group['GroupId'])
except:
    print("Security group not found")
else:
    print("Security group deleted")

# List of CloudWatch Logs groups to delete
log_group_names = ["/aws/lambda/sample-app-dev-consumer"]

# Delete specified CloudWatch Logs groups
try:
    log_groups = cloudwatch.describe_log_groups()['logGroups']
    for log_group in log_groups:
        if log_group['logGroupName'] in log_group_names:
            cloudwatch.delete_log_group(logGroupName=log_group['logGroupName'])
except:
    print("Logs groups not found")
else:
    print("Logs groups deleted")

# List of CloudTrails to delete
trail_names = ["tf-trail-elastic"]

# Delete specified CloudTrails
try:
    trails = cloudtrail.describe_trails()['trailList']
    for trail in trails:
        if trail['Name'] in trail_names:
            cloudtrail.delete_trail(Name=trail['Name'])
except:
    print("CloudTrails not found")
else:
    print("CloudTrails deleted")
    
# List of SQS queues to delete
queue_names = ["s3-cloudtrail-event-notification-queue", "s3-elb-event-notification-queue", "s3-s3-event-notification-queue", "s3-vpc-event-notification-queue"]

# Delete specified SQS queues
try:
    queues = sqs.list_queues()
    for queue in queues['QueueUrls']:
        for queue_name in queue_names:
            if queue_name in queue:
                sqs.delete_queue(QueueUrl=queue)
except:
    print("SQS queues not found")
else:
    print("SQS queues deleted")