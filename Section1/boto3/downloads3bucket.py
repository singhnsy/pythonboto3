import boto3
## Boto3 is the module for aws which contains all the functionalty, to connect and intract with aws services

# Create an s3 client
s3 = boto3.client('s3')     ## specificly we want this client should work for s3 services in aws

filename =  'boto3s3.txt'
bucket_name = 'devsecops-lab-2026'
destfile = 'botonewfile1'
s3.download_file(bucket_name, filename, destfile)
print("filedownload")