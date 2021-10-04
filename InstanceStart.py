import boto3
import json
instances = []
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Lifecycle',
            'Values': [
                'true'
            ]
        }
    ]
    )
    print('Output')
    print(response)
    print("/n")
    print(response['Reservations'])
    for reservation in response['Reservations']:
        print('Started INSTANCE')
        for instance in reservation['Instances']:
            print(instance['InstanceId'])
            instances.append(instance['InstanceId'])
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances: ' + str(instances))
