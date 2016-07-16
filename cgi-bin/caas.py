#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"

import os
import cgi,commands,re,cgitb
import mysql.connector as mariadb





x=cgi.FieldStorage()
name=x.getvalue('n')
type1=x.getvalue('t')
n=x.getvalue('no')
num=int(n)

while(num):

  d=commands.getstatusoutput("sudo docker run -itd --name {}{} {} bash".format(name,num,type1))
  a=commands.getstatusoutput("sudo docker ps | grep {}{} ".format(name,num))
  q=a[1]
  cid=q[:12]
  b=commands.getstatusoutput("sudo docker attach {}".format(cid))
  c=commands.getstatusoutput("sudo docker exec {} hostname -i".format(cid))
  ip=c[1]
  r=os.chdir("/var/www/html")
  e=commands.getstatusoutput("sudo echo \"<a href=\"http://{}:4200\" target=\"_blank\">{}</a><br>\" >> ct.html".format(ip,ip))
  num=num-1
print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.43.80/ct.html\">"

