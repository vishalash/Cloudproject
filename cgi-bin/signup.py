#!/usr/bin/python
import os,sys
import cgi,commands
import mysql.connector as mariadb

print"content-type:text/html"
print "\n"

x=cgi.FieldStorage()
name=x.getvalue('name')
email=x.getvalue('email')
password=x.getvalue('password')



mariadb_connection = mariadb.connect(user='root', password='ash12', database='fabbadal')
cursor = mariadb_connection.cursor()

try:
  cursor.execute("INSERT INTO user (name,email,password) VALUES (%s,%s,%s)", (name,email,password))
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

cursor.execute("SELECT name,email,password FROM user WHERE name=%s",(name,))


for name, email,password in cursor:
    print("<!--name: {}, email: {} , password: {} -->").format(name,email,password)
    print """
	<script>
	alert("Your account is now created")
	</script>
	<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80\">
	"""
mariadb_connection.close()


raw_input()
