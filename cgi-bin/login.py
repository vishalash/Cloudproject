#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"

from os import environ
import cgi,commands,re,cgitb
import mysql.connector as mariadb




x=cgi.FieldStorage()
email1=x.getvalue('email')
password1=x.getvalue('password')





mariadb_connection = mariadb.connect(user='root', password='ash12', database='fabbadal')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT email, password FROM user WHERE email=%s",(email1,))


for email, password in cursor:
   print "Set-Cookie:UserID={};\r\n".format(email)
   print "Set-Cookie:Password={};\r\n".format(password)

mariadb_connection.close()



if password == password1 :
  print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80/welcome.html\">"
else:
  print """
	<script>
	alert("Try Again")
	</script>
	<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80\">
	"""
