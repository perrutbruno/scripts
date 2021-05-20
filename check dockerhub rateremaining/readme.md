#Dockerhub REMAINING

create a schedule (usually cron, rundeck, etc) to run this script and be happy. 

It aims to check ***dockerhub's rate remaining value*** of your account. You should set you ***user*** and ***pass*** inside the script.

Check the value collect inside ```/opt/output_script2``` as a linux user

OR

#Zabbix integration
Treat it as External check and you'll be fine, no need to create user_params inside agent's config.
