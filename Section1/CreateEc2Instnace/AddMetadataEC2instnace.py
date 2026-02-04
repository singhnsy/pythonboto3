import boto3

# Step 1: Create an EC2 Resources
ec2_resource = boto3.resource('ec2')

#Step 2: Launch an EC2 instnaces

instances = ec2_resource.create_instances(
    ImageId = 'ami-0e2c8caa4b6378d8c',
    MinCount = 1,
    MaxCount = 1, 
    InstanceType = 't2.micro',
    KeyName = 'boto3ec2',
    BlockDeviceMappings = [
        { 
            'DeviceName' : '/dev/sda1',
            'Ebs' : {
                'VolumeSize': 20,
                'VolumeType': 'gp2',
                'DeleteOnTermination' : False
            }
        }
    ],

    TagSpecifications = [
        {
            'ResourceType' : 'instance',
            'Tags' : [ { 'Key' : 'Name', 'Value' : 'FinalEC2', }, { 'Key' : 'Env', 'Value' : 'PreProd'} ]
        }
    ],

    UserData = '''#!/bin/bash
    #Update packages list
    sudo apt update -y
    # Install apahce2
    sudo apt install apache2 -y
    # Start apache service
    sudo systemctl start apache2
    #Enable apache2 service
    sudo systemctl enable apache2
    #Create simple index.html file
    echo "<html><body><h1>Welcome to the Aapach2 Server - Narendra Singh </h1></body></hrml>" | sudo tee /var/www/html/index.html
    #Allow Apahce from firewall
    sudo ufw allow 'Apache'
    ''',
    
    )

print("My Instnace has been created")