#!/usr/bin/python
import os,sys
import cgi,commands
import random
import mysql.connector as mariadb

print"content-type:text/html"
print "\n"

p=(random.randint(5900,8000))


x=cgi.FieldStorage()
fname=x.getvalue('fname')
lname=x.getvalue('lname')
email=x.getvalue('email')
password=x.getvalue('password')



mariadb_connection = mariadb.connect(user='root', password='ash12', database='fabbadal')
cursor = mariadb_connection.cursor()

try:
  cursor.execute("INSERT INTO user (port,fname,lname,email,password) VALUES (%s,%s,%s,%s,%s)", (p,fname,lname,email,password))
except mariadb.Error as error:
  print("<!--ERROR: {} -->".format(error))
  
  print """
	<script>
	alert("This email address is already taken")
	</script>
	<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80\">
  	"""
  sys.exit()
mariadb_connection.commit()

cursor.execute("SELECT port,fname,lname,email,password FROM user WHERE email=%s",(email,))


for port,fname,lname, email,password in cursor:
    print("<!--port: {},fname: {},lname: {}, email: {} , password: {} -->").format(port,fname,lname,email,password)
    a=commands.getstatusoutput("sudo useradd {}".format(p))
    b=commands.getstatusoutput("sudo echo {}  |sudo passwd {} --stdin".format(password,p))
    print """
	<script>
	alert("Your account is now created")
	</script>
	<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80\">
	"""
mariadb_connection.close()


raw_input()
