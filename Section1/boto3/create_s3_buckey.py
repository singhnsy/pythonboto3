import boto3
# ClientError is a specific class provided by Botocore (the engine inside boto3) 
# that allows your script to catch and handle errors sent back by AWS. Without it, 
# if something goes wrong, your script will crash with a massive wall of red text (a Traceback), 
# which would break an automated pipeline.
from botocore.exceptions import ClientError

def create_my_bucket(bucket_name, region=None):
    try:
        if region is None:
            # Create bucket in Default Region (us-east-1)
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # Creatre bucket in Specific Region
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name, 
                CreateBucketConfiguration=location
            )
        print(f"Success! Bucket'{bucket_name}' created.")
    
    except ClientError as e:
        print(f"ClentError: {e}")
    except Exception as e:
        print(f"An unexpected errror occured: {e}")

#-----Execution-----
# Note : Bucket name must be globally unique accross all of aws ! 
YOUR_BUCKET_NAME = "devsecops-lab-2026"
create_my_bucket(YOUR_BUCKET_NAME, region="us-west-2") 
#create_my_bucket(YOUR_BUCKET_NAME, region="us-west-2") 




