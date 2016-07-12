#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"


import os
import cgi,commands,re,cgitb
import mysql.connector as mariadb

a= os.chdir("/var/lib")
b= commands.getstatusoutput("pwd")
print b[1]

raw_input()
