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
b=commands.getstatusoutput("sudo mkfs.ext4  /dev/hdvg/{}".format(name))
c=commands.getstatusoutput("sudo mkdir /media/{}".format(name))
d=commands.getstatusoutput("sudo chmod 777 /media/{}".format(name))
e=commands.getstatusoutput("sudo mount /dev/hdvg/{} /media/{}".format(name,name))
f=commands.getstatusoutput("sudo touch {}.sh".format(name))
i1=commands.getstatusoutput("sudo chmod 777 /etc/exports")
j1=commands.getstatusoutput("sudo echo \"/media/"+name+" *(rw,no_root_squash)\n\" >> /etc/exports")
i2=commands.getstatusoutput("sudo systemctl restart rpcbind")
j2=commands.getstatusoutput("sudo systemctl restart nfs-server")


g="mkdir /media/"+name+"\n"
h="mount  192.168.43.80:/media/"+name+" /media/"+name


i=commands.getstatusoutput("sudo chmod 777 {}.sh".format(name))
j=commands.getstatusoutput("sudo echo \""+g+h+"\"> "+name+".sh")
k=commands.getstatusoutput("sudo tar -cvf {}.tar {}.sh".format(name,name))

l=commands.getstatusoutput("sudo chmod 777 {}.tar".format(name))
m=commands.getstatusoutput("sudo mv {}.tar /var/www/html/tar".format(name,name))

print "<a href=http://192.168.43.80/tar/"+name+".tar >click to mount</a>"


