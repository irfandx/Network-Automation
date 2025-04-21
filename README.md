# Network-Automation 

Network automation netmiko in Pnetlab

step

1. Set the device (4 router, 1 switch L2, 1 ubuntu client)
2. on ubuntu client, update and ugpgrade linux, install python 3 and netmiko
3. Config the devices and save
   
 
=======================================================================================================

sample router basic configuration :

R1#show running-config 
Building configuration...

  
Current configuration : 3039 bytes
!
version 15.6
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R1
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
ethernet lmi ce
!
!
!
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!
!
!
!
!
!
!
!
!
!
!
ip domain name ZYDTECH.LOCAL
ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
username admin password 0 admin1234
!
redundancy
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
interface Loopback0
 ip address 1.1.1.1 255.255.255.0
!
interface GigabitEthernet0/0
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/1
 ip address 192.168.10.2 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/2
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/3
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip ssh version 2
!
!
!
!
control-plane
!
banner exec ^C
[OUTPUT OMMITED]
!
line con 0
 password cisco
 login
line aux 0
line vty 0 4
 login local
 transport input ssh
!
no scheduler allocate
!
end


=======================================================================================================

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
