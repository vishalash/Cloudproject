#!/usr/bin/python

print "Content-type:text/html\r\n\r\n"


import os
import cgi,commands,re,cgitb
import mysql.connector as mariadb

x=cgi.FieldStorage()
iname=x.getvalue('n')
icpu=x.getvalue('c')
iram=x.getvalue('r')
itype=x.getvalue('t')
idisk=x.getvalue('h')
port1=x.getvalue('port')
print iname
print icpu
print iram
print itype
print idisk
print port1
o=int(port1)
p= o+1



mariadb_connection = mariadb.connect(user='root', password='ash12', database='fabbadal')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT port, password FROM user WHERE port=%s",(port1,))


for port, password in cursor:
   print "<Password={};\r\n".format(password)
   print "<port={};\r\n".format(port)
   q=str(port)
   print q
if q == port1 :
  print "hello"
  a= os.chdir("/var/lib/libvirt/images")
  print commands.getstatusoutput("sudo qemu-img  create -f qcow2 {}.qcow2  {}G".format(iname,idisk))
  print commands.getstatusoutput("sudo virt-install --vnc --vncport={} --vnclisten=0.0.0.0 --noautoconsole --name  {} --ram  {} --vcpu {}  --location ftp://192.168.43.80/pub/os/rhel7.1    --disk path=/var/lib/libvirt/images/{}.qcow2,size={}  --os-type linux --os-variant  rhel7  --hvm   ".format(port1,iname,iram,icpu,iname,idisk))
  b= os.chdir("/var/www/html/vnc/utils")
  print commands.getstatusoutput("sudo  ./launch.sh --listen {} --vnc 192.168.43.80:{}".format(p,port1))
  print "<script type=\"text/javascript\">alert(\"Port to view os is \"+{});   </script>".format(p)
  print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://www.ash.com:{}/vnc.html?host=www.ash.com&port={}\">".format(p,p)
  
else:
  print "bye"
mariadb_connection.close()


