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

cursor.execute("SELECT port, password FROM user WHERE email=%s",(email1,))


for port, password in cursor:
   print "<!--port={};\r\n-->".format(port)
   print "<!--Password={};\r\n-->".format(password)


if password == password1 :
  cursor.execute("SELECT port, password FROM user WHERE email=%s",(email1,))
  
  for port, password in cursor:
   print "<script type=\"text/javascript\">alert(\"Keep this Number \"+{});   </script>".format(port)
   print "<!--Password={};\r\n-->".format(password)


   print """
       
        <META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80/welcome.html\">"
        """
else:
  print """
	<script>
	alert("Your password is Incorrect")
	</script>
	<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80\">
	"""

mariadb_connection.close()
