#!/usr/bin/python3.6
import datetime
import sys
import pdb
from optparse import OptionParser
import boto3

#Setting up dict with rds families. You should really consider this list as outdated, as it was written in 07-2020
rds_types_dict = {"db.t3.micro": 1,
                  "db.t2.micro": 1,
                  "db.t1.micro": 0.613,
                  "db.t2.small": 2,
                  "db.t3.small": 2,
                  "db.m1.small": 1.7,
                  "db.t2.medium": 4,
                  "db.t3.medium": 4,
                  "db.cv11.medium": 2,
                  "db.cv11.small": 1,
                  "db.mv11.medium": 4,
                  "db.m3.medium": 3.75,
                  "db.m1.medium": 3.75,
                  "db.t3.large": 8,
                  "db.t2.large": 8,
                  "db.rv11.large": 16, 
                  "db.cv11.large": 4,
                  "db.mv11.large": 8,
                  "db.m5.large": 8,
                  "db.m4.large": 8,
                  "db.m3.large": 7.5,
                  "db.m1.large": 7.5,
                  "db.r3.large": 15.25,
                  "db.r5.large": 16,
                  "db.r4.large": 15.25,
                  "db.t3.xlarge": 16,
                  "db.t2.xlarge": 16,
                  "db.m2.xlarge": 17.1,
                  "db.cv11.xlarge": 8,
                  "db.mv11.xlarge": 16,
                  "db.rv11.xlarge": 32,
                  "db.m5.xlarge": 16,
                  "db.m4.xlarge": 16,
                  "db.m3.xlarge": 15,
                  "db.m1.xlarge": 15,
                  "db.r3.xlarge": 30.5,
                  "db.r5.xlarge": 32,
                  "db.r4.xlarge": 30.5,
                  "db.t3.2xlarge": 32,
                  "db.t2.2xlarge": 32,
                  "db.m2.2xlarge": 34.2,
                  "db.rv11.2xlarge": 64,
                  "db.mv11.2xlarge": 32,
                  "db.cv11.2xlarge": 16,
                  "db.m5.2xlarge": 32,
                  "db.m4.2xlarge": 32,
                  "db.m3.2xlarge": 30,
                  "db.r3.2xlarge": 61,
                  "db.r5.2xlarge": 64,
                  "db.r4.2xlarge": 61,
                  "db.m2.4xlarge": 68.4,
                  "db.cv11.4xlarge": 32,
                  "db.rv11.4xlarge": 128,
                  "db.mv11.4xlarge": 64,
                  "db.m5.4xlarge": 64,
                  "db.m4.4xlarge": 64,
                  "db.r3.4xlarge": 122,
                  "db.r4.4xlarge": 122,
                  "db.r5.4xlarge": 128,
                  "db.cv11.9xlarge": 72,
                  "db.m4.10xlarge": 160,
                  "db.r3.8xlarge": 244,
                  "db.r4.8xlarge": 244,
                  "db.rv11.12xlarge": 384,
                  "db.mv11.12xlarge": 192,
                  "db.m5.12xlarge": 192,
                  "db.m4.16xlarge": 256,
                  "db.r5.12xlarge": 384,
                  "db.cv11.18xlarge": 144,
                  "db.r4.16xlarge": 488,
                  "db.mv11.24xlarge": 384,
                  "db.rv11.24xlarge": 768,
                  "db.m5.24xlarge": 384,
                  "db.r5.24xlarge": 768,
                  "db.x1e.8xlarge": 976,
                  "db.x1e.2xlarge": 244,
                  "db.r5.16xlarge": 512,
                  "db.x1e.32xlarge": 3904,
                  "db.z1d.2xlarge": 64,
                  "db.z1d.xlarge": 32,
                  "db.x1e.xlarge": 122,
                  "db.m5.16xlarge": 256,
                  "db.m5.8xlarge": 128,
                  "db.z1d.6xlarge": 192,
                  "db.z1d.12xlarge": 384,
                  "db.x1.16xlarge": 976,
                  "db.r5.8xlarge": 256,
                  "db.z1d.large": 16,
                  "db.z1d.3xlarge": 96,
                  "db.x1e.16xlarge": 1952,
                  "db.x1.32xlarge": 1952,
                  "db.x1e.4xlarge": 488,
                  "db.m6g.large": 8
                  }

### Arguments
parser = OptionParser()
parser.add_option("-i", "--instance-id", dest="instance_id",
                help="DBInstanceIdentifier")
parser.add_option("-a", "--access-key", dest="access_key",
                help="AWS Access Key")
parser.add_option("-k", "--secret-key", dest="secret_key",
                help="AWS Secret Access Key")
parser.add_option("-r", "--region", dest="region",
                help="RDS region")

(options, args) = parser.parse_args()

if (options.instance_id == None):
    parser.error("-i DBInstanceIdentifier is required")
if (options.access_key == None):
    parser.error("-a AWS Access Key is required")
if (options.secret_key == None):
    parser.error("-k AWS Secret Key is required")
###

### Get the region
if (options.region == None):
    options.region = 'us-east-1'

conn = boto3.client('rds', aws_access_key_id=options.access_key, aws_secret_access_key=options.secret_key, region_name=options.region)

response = conn.describe_db_instances( Filters=[{'Name': 'db-instance-id','Values': [options.instance_id,]}])

#Unpack the dict
for r in response['DBInstances']:
        db_memory_rds_name = r['DBInstanceClass']

        for rds in rds_types_dict:
            if rds == db_memory_rds_name:
                print(rds_types_dict[rds])
