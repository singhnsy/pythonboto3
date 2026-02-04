import boto3
## Boto3 is the module for aws which contains all the functionalty, to connect and intract with aws services

# Create an s3 client
s3 = boto3.client('s3')       ## specificly we want this client should work for s3 services in aws

# Specify the file to upload
filename = 'boto3s3.txt'
bucket_name = 'devsecops-lab-2026'
destfile = 'botonewfile1'     ## upload filename should be repace from boto3s3.txt with botonewfile1

s3.upload_file(filename, bucket_name, destfile)
#s3.upload_file(filename, bucket_name, filename)
print("file has been uploaded into the s3")