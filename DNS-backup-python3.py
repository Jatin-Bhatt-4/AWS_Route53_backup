import boto3
import json
import time
from datetime import datetime, timedelta, timezone
import os


# Set up clients for AWS Route53 and S3
route53 = boto3.client('route53')
s3 = boto3.client('s3')

# Get the list of hosted zones
hosted_zones = route53.list_hosted_zones()

# Iterate over the list of hosted zones
for hosted_zone in hosted_zones['HostedZones']:
    # Get the zone details
    zone_id = hosted_zone['Id']
    zone_name = hosted_zone['Name']

    # Export the hosted zone
    zone_response = route53.get_hosted_zone(Id=zone_id)
    zone = zone_response['HostedZone']

    # Get the resource record sets of the hosted zone
    resource_record_sets_response = route53.list_resource_record_sets(HostedZoneId=zone_id)
    resource_record_sets = resource_record_sets_response['ResourceRecordSets']

    # Set the bucket and folder name
    bucket_name = 'devops'
    folder_name = 'route53_backup/'
    # Get the list of objects in the folder
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)


    # Iterate over the objects
    for obj in objects.get('Contents', []):
        key = obj['Key']
        last_modified = obj['LastModified']
        age = (datetime.utcnow() - last_modified.replace(tzinfo=None)).days

        # Check if the object is older than 30 days
        if age > 30:
            # Delete the object
            s3.delete_object(Bucket=bucket_name, Key=key)
            print(f'{key} deleted from S3 as it is older than 30 days')
        else:
            print(f'{key} is not older than 30 days')
    # Set the file name
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_name = f'{zone["Name"]}_{timestr}.json'
    result = list()


    # Open the file in write mode
    with open(file_name, 'w') as f:
        # Write the zone and resource record sets to the file
        result.append(zone)
        result.append(resource_record_sets)
        f.write(json.dumps(result))
    # Upload the file to S3
    s3.upload_file(file_name, bucket_name, folder_name+file_name)
#    print(f'{file_name} has been uploaded to {bucket_name}/{folder_name}')
    os.remove(file_name)
#    print(f'{file_name} has been deleted from local after uploading to S3')
