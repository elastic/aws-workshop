import boto3
import json

# Set the AWS region
region_name = "us-east-2"

# Initialize the clients
ec2 = boto3.client('ec2', region_name=region_name)
cloudwatch = boto3.client('logs', region_name=region_name)
cloudtrail = boto3.client('cloudtrail', region_name=region_name)
sqs = boto3.client('sqs', region_name=region_name)

print("Delete EC2 instances if available")
# List of instance names to delete
instance_names = ["elastic-agent", "elastic-app"]

# Get instances with matching names
response = ec2.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': instance_names}])

# Delete instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        ec2.terminate_instances(InstanceIds=[instance_id])

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

# Initialize an S3 client
s3 = boto3.client("s3", region_name=region_name)
s3r = boto3.resource("s3", region_name=region_name)

# List of S3 bucket names to be emptied and deleted
buckets = ["sample-app-dev", "elastic-sar-bucket"]


for bucket_prefix in buckets:
    print('Try to delete buckets with prefix %s', bucket_prefix)

    # get a list of all buckets
    response = s3.list_buckets()

    for bucket in response['Buckets']:
        if bucket['Name'].startswith(bucket_prefix):

            bucket_region = s3.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint']
            if not bucket_region:
                bucket_region = 'us-east-1'  # default to us-east-1 if no region is specified
            if bucket_region != s3.meta.region_name:
                continue

            bucket_name = bucket['Name']
            # Add a bucket policy to deny all write operations
            bucket_policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "DenyWriteOperations",
                        "Effect": "Deny",
                        "Principal": "*",
                        "Action": [
                            "s3:PutObject",
                            "s3:PutObjectAcl",
                            "s3:PutObjectVersionAcl",
                            "s3:PutObjectTagging",
                        ],
                        "Resource": f"arn:aws:s3:::{bucket_name}/*"
                    }
                ]
            }            

            print('Put Bucket policy')
            s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))

            # List all objects in the bucket
            while (True) :
                print('Trigger object versions delete')
                bucket = s3r.Bucket(bucket_name)
                bucket.object_versions.delete()

                try:
                    objects = s3.list_objects(Bucket=bucket_name)["Contents"]
                    # Loop through all the objects in the bucket and delete them
                    print('Start to empty the Bucket for %s objects', len(objects))
                    count = 0
                    for obj in objects:
                        if count % 100 == 0 :
                            print('Deleted %s out of %s', count, len(objects))
                        s3.delete_object(Bucket=bucket_name, Key=obj["Key"])
                        count = count + 1
                except:
                    print('Bucket is empty')
                
                try:
                    print('Delete the Bucket')
                    # Once all objects are deleted, delete the bucket policy and the bucket
                    s3.delete_bucket_policy(Bucket=bucket_name)
                    s3.delete_bucket(Bucket=bucket_name)
                except:
                    print('Bucket still not empty')
                    continue
                else:
                    break

print('Delete CloudFormation Stack')
# create a CloudFormation client object
cloudformation = boto3.client('cloudformation', region_name=region_name)

# specify the name of the stack that you want to delete
stack_name = 'sample-app-dev'

# delete the stack
try:
    response = cloudformation.delete_stack(StackName=stack_name)
except:
    print("cloudformation stack not found")
else:
    print("cloudformation stack deleted")