#!/usr/bin/python
import os
import cgi,commands
print"content-type:text/html"
print""

#print "<font color=white>"
x=cgi.FieldStorage()
size=x.getvalue('i')
name=x.getvalue('n')

a=commands.getstatusoutput("sudo lvcreate --size {} --name {} hdvg".format(size,name))


b=commands.getstatusoutput("sudo chmod 777 /etc/tgt/targets.conf")
c=commands.getstatusoutput("sudo echo \"<target {}iqn> \" >> /etc/tgt/targets.conf".format(name))
d=commands.getstatusoutput("sudo echo \" backing-store /dev/hdvg/{} \" >> /etc/tgt/targets.conf".format(name))
e=commands.getstatusoutput("sudo echo \"</target> \" >> /etc/tgt/targets.conf")
f=commands.getstatusoutput("sudo systemctl restart tgtd")


g="yum install iscsi-initiator-utils\n"
h="iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.80 --discover\n"
i="iscsiadm --mode node --targetname "+name+"iqn --portal 192.168.43.80:3260 --login"

f1=commands.getstatusoutput("sudo touch {}block.sh".format(name))
i1=commands.getstatusoutput("sudo chmod 777 {}block.sh".format(name))
j=commands.getstatusoutput("sudo echo \""+g+h+i+"\"> "+name+"block.sh")
k=commands.getstatusoutput("sudo tar -cvf {}block.tar {}block.sh".format(name,name))

l=commands.getstatusoutput("sudo chmod 777 {}block.tar".format(name))
m=commands.getstatusoutput("sudo mv {}block.tar /var/www/html/tar".format(name,name))

print "<a href=http://192.168.43.80/tar/"+name+"block.tar >GET IT</a>"


       #Logout:

i="iscsiadm --mode node --targetname "+name+"iqn --portal 192.168.43.80:3260 --logout"
f1=commands.getstatusoutput("sudo touch {}blocklo.sh".format(name))
i1=commands.getstatusoutput("sudo chmod 777 {}blocklo.sh".format(name))
j=commands.getstatusoutput("sudo echo \""+i+"\"> "+name+"blocklo.sh")
k=commands.getstatusoutput("sudo tar -cvf {}blocklo.tar {}blocklo.sh".format(name,name))

l=commands.getstatusoutput("sudo chmod 777 {}blocklo.tar".format(name))
m=commands.getstatusoutput("sudo mv {}blocklo.tar /var/www/html/tar".format(name,name))

print "<a href=http://192.168.43.80/tar/"+name+"blocklo.tar >LOGOUT</a>"



