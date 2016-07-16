#!/usr/bin/python
import os
import cgi,commands
print"content-type:text/html"
print""

x=cgi.FieldStorage()
sw=x.getvalue('v')
f=open("/var/www/cgi-bin/db.txt","r")
name=f.read()

f="ssh -X -l "+name+" 192.168.100.1 gnome-terminal"

i1=commands.getstatusoutput("sudo touch {}terminal.sh".format(name))
i=commands.getstatusoutput("sudo chmod 777 {}terminal.sh".format(name))
j=commands.getstatusoutput("sudo echo \""+f+"\"> "+name+"terminal.sh")
k=commands.getstatusoutput("sudo tar -cvf {}terminal.tar {}terminal.sh".format(name,name))
l=commands.getstatusoutput("sudo chmod 777 {}terminal.tar".format(name))
m=commands.getstatusoutput("sudo mv {}terminal.tar /var/www/html/tar".format(name,name))
print "<a href=http://192.168.100.1/tar/"+name+"terminal.tar >GET</a>"


