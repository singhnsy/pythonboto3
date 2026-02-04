import boto3
## Boto3 is the module for aws which contains all the functionalty, to connect and intract with aws services

# Create an s3 client
s3 = boto3.client('s3')     ## specificly we want this client should work for s3 services in aws


#List all the buckets
response = s3.list_buckets()      # this is api call with aws s3
#print(response["Buckets"])
for i in response["Buckets"]:
    print(i["Name"])

