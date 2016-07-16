#!/usr/bin/python
import os
import cgi,commands
print"content-type:text/html"
print""

x=cgi.FieldStorage()
name=x.getvalue('port')
sw=x.getvalue('saas')


f="ssh -X -l "+name+" 192.168.43.80 "+sw

i1=commands.getstatusoutput("sudo touch {}{}.sh".format(name,sw))
i=commands.getstatusoutput("sudo chmod 777 {}{}.sh".format(name,sw))
j=commands.getstatusoutput("sudo echo \""+f+"\"> "+name+sw+".sh")
k=commands.getstatusoutput("sudo tar -cvf {}{}.tar {}{}.sh".format(name,sw,name,sw))
l=commands.getstatusoutput("sudo chmod 777 {}{}.tar".format(name,sw))
m=commands.getstatusoutput("sudo mv {}{}.tar /var/www/html/tar".format(name,sw))
print "<a href=http://192.168.43.80/tar/"+name+sw+".tar >GET</a>"


