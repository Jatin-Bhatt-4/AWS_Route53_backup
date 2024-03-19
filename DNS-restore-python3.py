
import boto3
from botocore.exceptions import ClientError
import json
import uuid
import sys

filename = input("Enter backup filename to restore on Route53: ")
if not filename:
    print("Please enter a valid file name.")
    exit()

# Creating Client & Resources
route53 = boto3.client('route53')
s3 = boto3.resource('s3')
folder_name = 'test_backup/'

# Reading file from S3 Bucket
print('RESTORING BACKUP')
obj = s3.Object('birdeye-devops', folder_name+filename)
file_contents = obj.get()['Body'].read().decode('utf-8')
file_contents = json.loads(file_contents)


# Getting ID of Hosted Zone
def get_hostedzone_id(file_contents):
    # Get the list of hosted zones
    hosted_zones = route53.list_hosted_zones()
    zone = list(filter(lambda zone: zone.get('Name') == file_contents[0].get('Name'), hosted_zones['HostedZones']))
    return zone


# Creating Hosted Zone if already doesn't Exists
def create_hosted_zone(file_contents):
    try:
        zone_id = get_hostedzone_id(file_contents)
        if len(zone_id) != 0:
            return "Zone Already Exists",202

        return route53.create_hosted_zone(
        Name = file_contents[0].get("Name"),
        CallerReference = str(uuid.uuid1())), 200
    except ClientError as err:
        return err, 409
             

# Creating DNS Record Sets
def create_resource_recordset(zone_id,file_contents):
    changes = list()
    for content in file_contents:
        payload = {
            'Action': "UPSERT",
            'ResourceRecordSet': content
        }

        changes.append(payload)

    return route53.change_resource_record_sets(
    HostedZoneId=zone_id,
    ChangeBatch={'Comment': 'Restored by Python', 'Changes': changes }
)


# Main Function to Restore Backup
def restore():
    try:    
        response, status= create_hosted_zone(file_contents)

        if status == 409 or status == 202:
            zone_id = get_hostedzone_id(file_contents)[0].get('Id')
            resource = create_resource_recordset(zone_id,file_contents[1])
        print('BACKUP RESTORATION COMPLETE')
    except ClientError as err:
        print(err)
restore()

