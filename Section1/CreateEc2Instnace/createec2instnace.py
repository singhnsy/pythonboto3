import boto3

# Step 1: Create an EC2 Resources
ec2_resource = boto3.resource('ec2')

#Step 2: Launch an EC2 instnaces

instances = ec2_resource.create_instances(
    ImageId = 'ami-01816d07b1128cd2d',
    MinCount = 1,
    MaxCount = 1, 
    InstanceType = 't2.micro',
    KeyName = 'boto3ec2',
    TagSpecifications = [
        {
            'ResourceType' : 'instance',
            'Tags' : [ { 'Key' : 'Name', 'Value' : 'MyEC2Boto2Instnace', }, { 'Key' : 'Env', 'Value' : 'Test'} ]
        }
    ]
)

print("My Instnace has been created")