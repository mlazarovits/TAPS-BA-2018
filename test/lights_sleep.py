import pyenttec as dmx
from time import sleep

port = dmx.select_port('/dev/tty.usbserial-ENVWHQLD')

def lights_sleep(chan1,chan2,chan3,chan4,chan5,chan6,chan7,chan8):
    while True:
       	port.blackout()
	port.render()
	sleep(2)

	i = chan1
	while i < chan2:
		b = 1
		while b <= 255:
			sleep(0.001)
			port.set_channel(i, b)
			#print "set channel " + str(i) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 1

	i = chan3
	while i < chan4:
		sleep(0.01)
		b = 1
		while b <= 255:
			sleep(0.001)
			port.set_channel(i, (255-b))
			port.set_channel((i+1), b)
			#print "set channel " + str(i) + " to " + str(100-b) + " and channel " + str(i+1) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 1


	i = chan5
	while i < chan6:
		sleep(0.01)
		b = 1
		while b <= 255:
			sleep(0.001)
			port.dmx_frame[(i+1)] = (255-b)
			port.dmx_frame[(i+2)] = b
			#print "set channel " + str((i+1)) + " to " + str(100-b) + " and channel " + str(i+2) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 1
	i = chan7
	while i < chan8:
		sleep(0.01)
		b = 1
		while b <= 255:
			sleep(0.001)
			port.dmx_frame[(i+1)] = (255-b)
			port.dmx_frame[(i+2)] = b
			#print "set channel " + str((i+1)) + " to " + str(100-b) + " and channel " + str(i+2) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 1	

	sleep(2)
lights_sleep(1,5,2,10,3,15,4,20)
#port.dmx_frame[47]= 99
#port.render()