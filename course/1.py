import signal

def lw(x,y):
	print "ok bye..."
	exit()

signal.signal(2,  lw)

x=raw_input("Enter your data \n ")
print x
