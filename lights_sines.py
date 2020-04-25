import pyenttec as dmx
from time import sleep
import math

port = dmx.select_port('/dev/tty.usbserial-ENVWHQLD')
#port.blackout()
#port.render()


def fixt3ch_set(startchan, r, g, b):
	port.dmx_frame[startchan] = r
	port.dmx_frame[(startchan+1)] = g
	port.dmx_frame[(startchan+2)] = b
	return True


port.render() 
i = 0 
while i < 2:
	b = (int(abs(math.sin(math.radians(i))) * 100))
	c = (int(abs(math.cos(math.radians(i))) * 100))
	#print "sin " + str(i) + " yields " + str(b)
	#print "cos " + str(i) + " yields " + str(c)	
	f = 0
	while f < 8:
		fixt3ch_set(f, b, b, b)
		fixt3ch_set((f+1), c, c, c)
		f = f + 2
	
	port.render()
	sleep(0.01)
	i = i + 1

o = 0
while o < 27:
	port.dmx_frame[o] = 0
	port.render()
	o = o + 1

# port.blackout()
# port.render()
#port.close()