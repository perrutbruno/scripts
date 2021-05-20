#aws RDS type

It aims to check ***RDS type*** of your database passed on CLI. You should set your params as stated: 
```rds_instance_memory_total.py["--instance-id","{HOST.HOST}","--access-key","{$AWS_ACCESS_KEY}","--secret-key","{$AWS_SECRET_KEY}","--region","{$REGION}"]```


#Zabbix integration
Treat it as External check and configure you macros like this:
{$AWS_ACCESS_KEY} = YOUR_ACCESS_KEY
{$AWS_SECRET_KEY} = YOUR_SECRET KEY
{$REGION} = us-east-1(example)
