import boto3
import json
import logging

# Initialize an S3 client
s3 = boto3.client("s3")
s3r = boto3.resource("s3")

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

# List of S3 bucket names to be emptied and deleted
buckets = ["<bucket_name>"]


for bucket_name in buckets:
    logging.info('Try to delete bucket %s', bucket_name)

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
    logging.info('Put Bucket policy')
    s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))

    # List all objects in the bucket
    while (True) :
        logging.info('Trigger object versions delete')
        bucket = s3r.Bucket(bucket_name)
        bucket.object_versions.delete()

        try:
            objects = s3.list_objects(Bucket=bucket_name)["Contents"]
            # Loop through all the objects in the bucket and delete them
            logging.info('Start to empty the Bucket for %s objects', len(objects))
            count = 0
            for obj in objects:
                if count % 100 == 0 :
                    logging.info('Deleted %s out of %s', count, len(objects))
                s3.delete_object(Bucket=bucket_name, Key=obj["Key"])
                count = count + 1
        except:
            logging.info('Bucket is empty')
        
        try:
            logging.info('Delete the Bucket')
            # Once all objects are deleted, delete the bucket policy and the bucket
            s3.delete_bucket_policy(Bucket=bucket_name)
            s3.delete_bucket(Bucket=bucket_name)
        except:
            logging.info('Bucket still not empty')
            continue
        else:
            break