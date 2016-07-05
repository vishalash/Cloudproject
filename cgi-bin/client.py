#!/usr/bin/python2
import os
os.system("tput setaf 1")
print"\t\t\t\t"

print"""
        press 1 for any software for rent
	press 2 for new Object Storage
        press 3 for new Block Storage
	press 4 for exit
	
"""
ch=raw_input("enter your choice:")
if int(ch)==1:
   
    print "software on rent"
    x=raw_input("Enter the Software you want to use")
    os.system("ssh -X -l root  10.42.0.211  {}".format(x))
if int(ch)==2:
     name=raw_input("Enter name of your Fab object storage")
     size=raw_input("Enter the Size you want in MiB")
     
    
     os.system("lvcreate --size {} --name {} hdvg".format(size,name))
     os.system("mkfs -t ext2 /hdvg/{}".format(name))
     os.system("mkdir /media/{}".format(name))
     os.system("chmod 777 /media/{}".format(name))
     os.system("mount /dev/hdvg/{} /media/{}".format(name,name))
   
     print" Fab Volume created"
    
         
  
 #    print"""
 #      press 1 for nfs
 #	press 2 for ssh
 #   """
 #    if int(pr)==1:
 #		os.system("mkdir /media/Fabbox")
 #               os.system("mount  10.42.0.211:/media/user /media/Fabbox")
 
 #    if int(pr)==2:
 #		os.system("sshfs root@ 10.42.0.211:/media/user /media/Fabbox") 
 
raw_input()
