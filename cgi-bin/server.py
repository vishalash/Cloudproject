#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"

import os
import cgi,commands,re,cgitb
import mysql.connector as mariadb




x=cgi.FieldStorage()
name=x.getvalue('n')
size=x.getvalue('s')
pro=x.getvalue('protocol')

mariadb_connection = mariadb.connect(user='root', password='ash12', database='fabbadal')
cursor = mariadb_connection.cursor()


os.system("lvcreate --name {} --size {}G /dev/hdvg".format(name,size))
os.system("mkdir /media/user")
os.system("mkfs.ext4 /dev/hdvg/{}".format(name))
os.system("mount /dev/hdvg/{} /media/user".format(name))
    
if int(pr)==1:
	os.system("vim /etc/exports")
		
if int(pr)==2:
	os.system("chmod 777 /media/user")

