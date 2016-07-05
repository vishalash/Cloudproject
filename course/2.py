import thread
import time
def a():
	while True:
		print "1"
		

def b():
	while True:
		print "2"
		

thread.start_new_thread( a,() )

thread.start_new_thread( b,())

raw_input()  
