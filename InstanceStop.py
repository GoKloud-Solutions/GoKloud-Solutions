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
        print('STOPPED INSTANCE')
        for instance in reservation['Instances']:
            print(instance['InstanceId'])
            instances.append(instance['InstanceId'])
    ec2.stop_instances(InstanceIds=instances)
    print('Stoped your instances: ' + str(instances))
