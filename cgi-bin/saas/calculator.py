#!/usr/bin/python
import os
import cgi,commands
print"content-type:text/html"
print""

x=cgi.FieldStorage()
sw=x.getvalue('v')
f=open("/var/www/cgi-bin/db.txt","r")
name=f.read()

f="ssh -X -l "+name+" 192.168.100.1 gnome-calculator"

i1=commands.getstatusoutput("sudo touch {}calculator.sh".format(name))
i=commands.getstatusoutput("sudo chmod 777 {}calculator.sh".format(name))
j=commands.getstatusoutput("sudo echo \""+f+"\"> "+name+"calculator.sh")
k=commands.getstatusoutput("sudo tar -cvf {}calculator.tar {}calculator.sh".format(name,name))
l=commands.getstatusoutput("sudo chmod 777 {}calculator.tar".format(name))
m=commands.getstatusoutput("sudo mv {}calculator.tar /var/www/html/tar".format(name,name))
print "<a href=http://192.168.100.1/tar/"+name+"calculator.tar >GET</a>"


