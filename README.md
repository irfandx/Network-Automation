# Network-Automation 

Network automation netmiko in Pnetlab

step

1. Set the device (4 router, 1 switch L2, 1 ubuntu client)
2. on ubuntu client, update and ugpgrade linux, install python 3 and netmiko
3. Config the devices and save

NOTE : also config "crypto key exchange" before enabling ip ssh version 2


=======================================================================================================

Connection test

ping host

ssh -o KexAlgorithms=+diffie-hellman-group14-sha1 admin@192.168.10.1
(since device image on this lab only accpept diffie-hellman key exchange)

ssh password : admin1234
exec password : cisco

=======================================================================================================

from ubuntu client, run the log_daily.py : python3 log_daily.py
