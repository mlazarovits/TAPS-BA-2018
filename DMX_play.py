#will need active dmx connection to see results, but not for debugging
#stage directions are from lightboard PoV
import pyenttec as dmx
port = dmx.select_port('/dev/tty.usbserial-ENVWHQLD')

#####################################################################
#center lights
#####################################################################
port.dmx_frame[0] = 0 #pink DC
port.dmx_frame[3] = 0 #rectangle C
port.dmx_frame[5] = 0 #pink!! UC
port.dmx_frame[24] = 0 #C bright wash

port.dmx_frame[4] = 0 #CL wash
port.dmx_frame[14] = 0 #CL same as 4
port.dmx_frame[19] = 0 #pinkish CL
port.dmx_frame[27] = 0 #CL wash
port.dmx_frame[29] = 0 #CL wash (broad)

port.dmx_frame[35] = 255 #CR faint rectangle
#####################################################################
#right
#####################################################################
port.dmx_frame[1] = 0 #UR corner wash
port.dmx_frame[6] = 0 #UR wash
port.dmx_frame[15] = 0 #rectangle UR
port.dmx_frame[16] = 0 #UR
port.dmx_frame[22] = 255 #pink UR corner wash

#####################################################################
#left
#####################################################################
port.dmx_frame[7] = 0 #UL spot
port.dmx_frame[8] = 0 #UL same as 7 but brighter
port.dmx_frame[9] = 0 #UL same as 7 but wash
port.dmx_frame[10] = 0 #UL same as 7 but brighter wash
port.dmx_frame[11] = 0 #UL same as 7
port.dmx_frame[25] = 0 #UL corner wash
port.dmx_frame[30] = 255 #pink UL spot
port.dmx_frame[31] = 0 #UL corner wash (on white silk)
port.dmx_frame[32] = 0 #bright UL corner spot
port.dmx_frame[34] = 0 #UL wash
port.dmx_frame[26] = 0 #very DL spot (on lightboard)
port.dmx_frame[17] = 0 #DL
port.dmx_frame[18] = 0 #pink DL
port.dmx_frame[20] = 0 #DL
port.dmx_frame[21] = 0 #DCL wash
port.dmx_frame[23] = 0 #DCL
port.dmx_frame[33] = 0 #DL wash (on piano)

#####################################################################
#dark
#####################################################################
#port.dmx_frame[2] = 255 #dark
#port.dmx_frame[13] = 255 #dark

#lightboard led DS
port.dmx_frame[36] = 99 #led red
port.dmx_frame[37] = 0 #led gren
port.dmx_frame[38] = 0 #led blue

#mirror led DS
port.dmx_frame[46] = 0 #led red
port.dmx_frame[47] = 0 #led green
port.dmx_frame[48] = 0 #led blue

#mirror led US
port.dmx_frame[56] = 0 #led red
port.dmx_frame[57] = 0 #led green
port.dmx_frame[58] = 0 #led red

#window led US
port.dmx_frame[66] = 0 #led red
port.dmx_frame[67] = 0 #led green
port.dmx_frame[68] = 0 #led red

#port.blackout()

port.render()


#########################################################################################################
#########################################################################################################
#keywords will be in a list
#it works!!!!


