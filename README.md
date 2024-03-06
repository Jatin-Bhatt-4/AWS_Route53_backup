# Route53 Backup to S3 Bucket

## Overview
This Python script is designed to backup Route53 hosted zones and their resource record sets to an Amazon S3 bucket. It ensures that older backups are deleted from the S3 bucket to manage storage efficiently. Each backup file is named with a timestamp appended to the hosted zone name for identification and versioning purposes.

## Requirements
* Python 3.x
* **boto3** library
* AWS credentials configured on the system

## Installation
1. Install the required dependencies using pip: **pip install boto3**
2. Configure AWS credentials on your system. You can do this by setting environment variables or using AWS CLI.

## Configuration
1. Modify the **bucket_name and folder_name** variables in the script to specify the S3 bucket and folder where backups will be stored.
2. Adjust the age threshold (age > 30) if you want to retain backups for a different duration.

## Usage
Run the following command inside the folder where program is placed-
**/usr/bin/python3 DNS-backup-python3.py**

## Author
- Created by Jatin Bhatt
