#!/usr/bin/python
# -*- coding: utf-8 -*-

#	shaney.py              by Greg McFarlane
#	                       some editing by Joe Strout
#
#	search for "Mark V.  Shaney" on the WWW for more info!

import numpy
import random
import Algorithmia #keywords
#import pysimpledmx
import pyttsx3 #text to speech
from time import sleep
import pyenttec as dmx #light cues
global port
port = dmx.select_port('/dev/tty.usbserial-ENVWHQLD')

#light cue functions
def lights_sleep():
    print('lights sleep')
    # while True:
    port.blackout()
    port.render()
    sleep(2)
    print('lights sleep')

    i = 0
    while i < 24:
    	b = 0
    	while b <= 100:
    		sleep(0.001)
    		port.set_channel(i, b)
    		#print "set channel " + str(i) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 3

    i = 0
    while i < 24:
    	sleep(0.01)
    	b = 0
    	while b <= 255:
    		sleep(0.001)
    		port.set_channel(i, (255-b))
    		port.set_channel((i+1), b)
    		#print "set channel " + str(i) + " to " + str(100-b) + " and channel " + str(i+1) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 3


    i = 0
    while i < 24:
    	sleep(0.01)
    	b = 0
    	while b <= 100:
    		sleep(0.001)
    		port.dmx_frame[(i+1)] = (100-b)
    		port.dmx_frame[(i+2)] = b
    		#print "set channel " + str((i+1)) + " to " + str(100-b) + " and channel " + str(i+2) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 3

    sleep(2)
    print('lights sleep')


def led_sleep():
    print('led sleep')
    # while True:
    port.blackout()
    port.render()
    sleep(2)
    print('led sleep')
    i = 36
    while i < 38:
    	b = 1
    	while b <= 100:
    		sleep(0.001)
    		port.set_channel(i, b)
    		#print "set channel " + str(i) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 1
    i = 46
    while i < 48:
    	b = 1
    	while b <= 100:
    		sleep(0.001)
    		port.set_channel(i, b)
    		#print "set channel " + str(i) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 1
    i = 56
    while i < 58:
    	b = 1
    	while b <= 100:
    		sleep(0.001)
    		port.set_channel(i, b)
    		#print "set channel " + str(i) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 1 
    i = 66
    while i < 68:
    	b = 1
    	while b <= 100:
    		sleep(0.001)
    		port.set_channel(i, b)
    		#print "set channel " + str(i) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 1 	
    sleep(2)
    print('led sleep')


def chans_sleep(chan1,chan2,chan3,chan4,chan5,chan6,chan7,chan8):
    print('chans sleep')
    # while True:
    port.blackout()
    port.render()
    sleep(2)

    print('chans sleep')

    i = chan1
    while i < chan2:
    	b = 1
    	while b <= 100:
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
    	while b <= 100:
    		sleep(0.001)
    		port.dmx_frame[(i+1)] = (100-b)
    		port.dmx_frame[(i+2)] = b
    		#print "set channel " + str((i+1)) + " to " + str(100-b) + " and channel " + str(i+2) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 1
    i = chan7
    while i < chan8:
    	sleep(0.01)
    	b = 1
    	while b <= 100:
    		sleep(0.001)
    		port.dmx_frame[(i+1)] = (100-b)
    		port.dmx_frame[(i+2)] = b
    		#print "set channel " + str((i+1)) + " to " + str(100-b) + " and channel " + str(i+2) + " to " + str(b)
    		port.render()
    		b = b + 1
    	i = i + 1	
    sleep(2)
    print('chans sleep')

def static_4cue(chan1,chan2,chan3,chan4):
    print('static')
    port.dmx_frame[chan1] = 255
    port.dmx_frame[chan2] = 255
    port.dmx_frame[chan3] = 255
    port.dmx_frame[chan4] = 255
    #port.blackout()
    #port.render()

#intialize Autotag algorithm
client = Algorithmia.client('simDowato8YdOWxUueFkB06Vdzu1')
algo = client.algo('nlp/AutoTag/1.0.1')

#initialize dmx connections
#dmx3 = pysimpledmx.DMXConnection(3)


def choice(words):
    #assumes words is non-empty
    random.seed
    index = random.randint(0,len(words)-1)
    return words[index]
   
   

def run(filename=''):
    if filename=='':
    	file = open( raw_input('Enter name of a textfile to read: '), 'r')
    else:
    	file = open( filename, 'r')

    text = file.read()
    file.close()
    # print(text)
    words = str.split(text)

    global total_markov
    total_markov = []
    	
    end_sentence = []
    dict = {}
    prev1 = ''
    prev2 = ''
    #prev3 = ''
    for word in words:
        if prev1 != '' and prev2 != '':
            key = (prev2, prev1)
            if key in dict:
            # if dict.has_key(key):
              dict[key].append(word)
            else:
              dict[key] = [word]
        if (prev1[-1:] == '.' or prev1[-1:] == '?' or prev1[-1:] == '!' or prev1[-1:] == ':'):
            end_sentence.append(key)     
        prev2 = prev1
        prev1 = word


    if end_sentence == []:
        print('Sorry, there are no sentences in the text.')
        return
      
    key = ()
    count = 10


    while 1:
        if key in dict:
      # if dict.has_key(key):
            word = choice(dict[key])
            file_finished = open('run/script_compiled','a')
            global output
            output = word + ' '
            file_finished.write(output) #here is where the individual words are written to the file
            print(output)  #each word 
            key = (key[1], word)
            total_markov.append(word) 
            if key in end_sentence:
                print('\n')
                count = count - 1
                key = choice(end_sentence)
                if count <= 0:
                	break
        else:
            key = choice(end_sentence) 
        


##########################################################################################
##########################################################################################

#cycle thru scripts, get keywords

#scripts are chopped up into scriptChoices/script_i.txt based on scene changes, etc.
#this part updates the script_compiled file as the run function cycles through words

file_finished = open('run/script_compiled','w')
for i in numpy.random.choice(22,1):  #total range is 0 to 23, how to choose which file to run markov chain on
    print('words taken from script #' + str(i))
    print('\n')
    filename =  'scriptChoices/script_' + str(i) + '.txt' 
    script_i = run(filename)   
    file_finished.write('\n')         
    file_finished = open('run/script_compiled','a') #add script chunk
    file_finished.write('\n\n')
    #print 
    input = ' '.join(total_markov)  #input for extracting keywords and text to speech
    
    #extracting keywords (list)
    global keywords
    keywords = algo.pipe(input).result 
    print('keywords have been generated')
    
    #writing keywords to external text file
    file_finished = open('run/keywords','a')
    
   
    print('\n')

    #port.blackout()
    #lights_sleep()
    c1 = int(numpy.random.choice(22,1))
    c2 = int(numpy.random.choice(22,1))
    c3 = int(numpy.random.choice(22,1))
    c4 = int(numpy.random.choice(22,1))
    static_4cue(c1, c2, c3, c4)
    port.render()  
       #text to speech

    print('speaking new script')
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-55)
    engine.say(input)
    engine.runAndWait()
       
print('script has been said')
print('begin light cues')

# These words were chosen by the directory based on frequency 
# of use and sentimental meaning to match to keywords

 	        
#light cues

    #triggering light cues (per script cut)
    #have set light cues for each keyword 
    

################################################################
    #names       
if any(word == "Sir" for word in keywords):
    static_4cue(16, 32, 17, 30)
    port.dmx_frame[22] = 255 
    static_4cue(36, 37, 38, 0) 
    port.render()             
if any(word == "Captain" for word in keywords):
    static_4cue(16, 32, 17, 30)
    port.dmx_frame[22] = 255 
    static_4cue(36, 37, 38, 0)
    port.render()  
       
if any(word == "Colonel" for word in keywords):
    static_4cue(16, 32, 17, 30)
    port.dmx_frame[22] = 255 
    static_4cue(36, 37, 38, 0)
    port.render()
        
                 
                          
################################################################                           
#grand verbs
if any(word == 'afford' for word in keywords):
    lights_sleep()
    port.render()
if any(word == 'being' for word in keywords):
    lights_sleep()
    port.render()       
if any(word == 'belong' for word in keywords):
    lights_sleep()   
    port.render()       
if any(word == 'come' for word in keywords):
    lights_sleep() 
    port.render()            
if any(word == 'coming' for word in keywords):
    lights_sleep()
    port.render()                                 
if any(word == 'remain' for word in keywords):
    lights_sleep() 
    port.render()  
if any(word == 'returning' for word in keywords):
    lights_sleep() 
    port.render()       
if any(word == 'settle' for word in keywords):
    lights_sleep() 
    port.render()                             
if any(word == 'shining' for word in keywords):
    lights_sleep()
    port.render()                                                       
if any(word == 'waiting' for word in keywords):
    lights_sleep()
    port.render()                                                                             
################################################################     
#active verbs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
if any(word == 'abandon' for word in keywords):
    led_sleep()   
    port.render()                                                                         
if any(word == 'accelerates' for word in keywords):
    led_sleep()  
    port.render()                                                                           
if any(word == 'brushed' for word in keywords):
    led_sleep()
    port.render()                                                                             
if any(word == 'dictate' for word in keywords):
    led_sleep()  
    port.render()                                                                           
if any(word == 'escape' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'lead' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'leave' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'listen' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'listened' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'meet' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'struggling' for word in keywords):
    led_sleep()  
    port.render()                                                                           
if any(word == 'transport' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'unlock' for word in keywords):
    led_sleep() 
    port.render()                                                                            
if any(word == 'usurp' for word in keywords):
    led_sleep() 
    port.render()                                                                            
################################################################
#earth verbs        
if any(word == 'remember' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12, 16, 0, 33)
    port.render() 
if any(word == 'dance' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12, 16, 0, 33)
    port.render()
if any(word == 'sing' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12, 16, 0, 33)
    port.render() 
if any(word == 'sleep' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12, 16, 0, 33)
    port.render() 
if any(word == 'legislate' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12, 16, 0, 33)
    port.render() 
if any(word == 'living' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12,16, 0, 33)
    port.render() 
if any(word == 'play' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12,16, 0, 33)
    port.render() 
if any(word == 'pray' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12 ,16, 0, 33)
    port.render() 
if any(word == 'sails' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12 ,16, 0, 33)
    port.render() 
if any(word == 'judge' for word in keywords):
    chans_sleep(9, 30, 3, 11, 12, 16, 0, 33)
    port.render() 
          
################################################################                
#adverbs                                                   
if any(word == 'behind' for word in keywords):
    port.dmx_frame[0] = 123
    port.render() 
if any(word == 'beyond' for word in keywords):
    port.dmx_frame[0] = 123  
    port.render()       
if any(word == 'direct' for word in keywords):
    port.dmx_frame[0] = 123  
    port.render()       
if any(word == 'perpetually' for word in keywords):
    port.dmx_frame[0] = 123 
    port.render()        
if any(word == 'underweighs' for word in keywords):
    port.dmx_frame[0] = 123
    port.render()         
if any(word == 'withered' for word in keywords):
    port.dmx_frame[0] = 123  
    port.render()       
################################################################        
#earth pop culture        
if any(word == 'American' for word in keywords):
    lights_sleep()   
    port.render() 
if any(word == 'National' for word in keywords):
    lights_sleep()   
    port.render()     
if any(word == 'ball' for word in keywords):
    lights_sleep()   
    port.render()        
if any(word == 'baseball' for word in keywords):
    lights_sleep()   
    port.render()             
if any(word == 'business' for word in keywords):
    lights_sleep()   
    port.render()                
if any(word == 'Dodgers' for word in keywords):
    lights_sleep()   
    port.render()                     
if any(word == 'television' for word in keywords):
    lights_sleep()   
    port.render() 
if any(word == 'soda' for word in keywords):
    port.dmx_frame[0] = 123 
    port.render()        
if any(word == 'chocolate' for word in keywords):
     lights_sleep()   
     port.render()                             
if any(word == 'schools' for word in keywords):
    lights_sleep()   
    port.render()                                                    
if any(word == 'camera' for word in keywords):
    lights_sleep()   
    port.render() 
  
################################################################
#nature light/fire
if any(word == 'twilight' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)
    port.render()
if any(word == 'shadow' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'shadowed' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()        
#nature earth
if any(word == 'cave' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'canyon' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'autumn' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'craggy' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'crops' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'farm' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'farmed' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'farming' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'sheep' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'flats' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()  
if any(word == 'flower' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'petals' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'plants' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()  
if any(word == 'trees' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'forests' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()  
if any(word == 'garden' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()  
if any(word == 'ground' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'hillsides' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'leaves' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'magnesium' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'salt' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()  
if any(word == 'mountains' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()    
if any(word == 'root' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'sap' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'seeds' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
#nature water
if any(word == 'water' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'lakes' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'rain' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'rainfall' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)#CR faint rectangle
    port.render()  
if any(word == 'rivers' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'seas' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
#nature air/sky
if any(word == 'clouds' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()
if any(word == 'mist' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'wind' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'storm' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'winter' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'sky' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
#nature senses
if any(word == 'seasons' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()  
if any(word == 'weather' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()   
if any(word == 'diseases' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render() 
if any(word == 'viruses' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #CR faint rectangle
    port.render()      
################################################################
#earth places        
if any(word == 'Los Angeles' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)
    port.render() 
if any(word == 'California' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'Earth' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'New York' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()     
if any(word == 'Oregon' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)  
    port.render()       
if any(word == 'Wisconsin' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) 
    port.render()            
################################################################
#color               
if any(word == 'black' for word in keywords):
    led_sleep()
    port.render() 
if any(word == 'blue' for word in keywords):
    led_sleep() 
    port.render()                          
if any(word == 'clear' for word in keywords):
    led_sleep() 
    port.render()  
if any(word == 'color' for word in keywords):
    led_sleep() 
    port.render()   
if any(word == 'gold' for word in keywords):
    led_sleep() 
    port.render()                          
if any(word == 'green' for word in keywords):
    led_sleep()
    port.render()  
if any(word == 'lit' for word in keywords):
    led_sleep() 
    port.render()   
if any(word == 'orange' for word in keywords):
    led_sleep()   
    port.render()                         
if any(word == 'red' for word in keywords):
    led_sleep()   
    port.render()  
if any(word == 'sparkling' for word in keywords):
    led_sleep()   
    port.render()   
if any(word == 'velvet' for word in keywords):
    led_sleep()   
    port.render()                          
if any(word == 'white' for word in keywords):
    led_sleep()   
    port.render()                               
                                    
################################################################                                                        
#time
if any(word == 'calendar' for word in keywords):
    lights_sleep() #UR wash
    port.render() 
if any(word == 'clock' for word in keywords):
    lights_sleep() #UR wash   
    port.render()      
if any(word == 'day' for word in keywords):
    lights_sleep() #UR wash 
    port.render()        
if any(word == 'days' for word in keywords):
    lights_sleep() #UR wash  
    port.render()       
if any(word == 'minutes' for word in keywords):
    lights_sleep() #UR wash  
    port.render()       
if any(word == 'month' for word in keywords):
    lights_sleep() #UR wash
    port.render() 
if any(word == 'months' for word in keywords):
    lights_sleep() #UR wash  
    port.render()       
if any(word == 'thursday' for word in keywords):
    lights_sleep() #UR wash  
    port.render()       
if any(word == 'today' for word in keywords):
    lights_sleep() #UR wash  
    port.render()       
if any(word == 'tomorrow' for word in keywords):
    lights_sleep() #UR wash  
    port.render()     
if any(word == 'wednesday' for word in keywords):
    lights_sleep() #UR wash
    port.render() 
if any(word == 'week' for word in keywords):
    lights_sleep() #UR wash 
    port.render()        
if any(word == 'years' for word in keywords):
    lights_sleep() #UR wash 
    port.render()        
if any(word == 'ancient' for word in keywords):
    lights_sleep() #UR wash  
    port.render()       
if any(word == 'old' for word in keywords):
    lights_sleep() #UR wash   
    port.render()            
if any(word == 'older' for word in keywords):
    lights_sleep() #UR wash  
    port.render()         
if any(word == 'growth' for word in keywords):
   lights_sleep() #UR wash  
   port.render()         
if any(word == 'late' for word in keywords):
    lights_sleep() #UR wash  
    port.render()         
if any(word == 'modern' for word in keywords):
    lights_sleep() #UR wash  
    port.render()         
if any(word == 'morning' for word in keywords):
    lights_sleep() #UR wash 
    port.render()   
if any(word == 'now' for word in keywords):
    lights_sleep() #UR wash  
    port.render()          
if any(word == 'once' for word in keywords):
    lights_sleep() #UR wash  
    port.render()                  
if any(word == 'time' for word in keywords):
    lights_sleep() #UR wash  
    port.render() 
if any(word == 'times' for word in keywords):
    lights_sleep() #UR wash  
    port.render()                         
if any(word == 'wait' for word in keywords):
    lights_sleep() #UR wash  
    port.render() 
if any(word == 'waiting' for word in keywords):
    lights_sleep() #UR wash  
    port.render()                                                        
if any(word == 'moment' for word in keywords):
    lights_sleep() #UR wash  
    port.render()                                                                      
################################################################
#divine                                                                                                                                                                                                
if any(word == 'blasphemy' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                                                                            
if any(word == 'fate' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'phantom' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'God' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()               
if any(word == 'heaven' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()               
if any(word == 'Lord' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                               
if any(word == 'messiah' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
################################################################       
#space       
if any(word == 'radar' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'galaxy' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'meteor' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'moon' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'night' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()       
if any(word == 'rockets' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'ship' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'ships' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()          
if any(word == 'signal' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()          
if any(word == 'skies' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'space' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'stars' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render()
if any(word == 'sun' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()       
if any(word == 'suns' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render() 
                    
################################################################################################################################                                           
#society
if any(word == 'message' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                             
if any(word == 'welcoming' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                 
if any(word == 'wishful' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                                  
if any(word == 'adults' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                                                                         
if any(word == 'animals' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                       
if any(word == 'eyes' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()                                         
if any(word == 'farewells' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'good-bye' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'guide' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()           
if any(word == 'harm' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'individuals' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()        
if any(word == 'lonely' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'loneliness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'man' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()         
if any(word == 'name' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()  
if any(word == 'skin' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'suns' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render() 
if any(word == 'sleep' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'woman' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()             
if any(word == 'remnant' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()    
if any(word == 'things' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()        
if any(word == 'key' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == '402' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()       
if any(word == 'requirements' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'compound' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'bunker' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()              
if any(word == 'burial' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                       
if any(word == 'cities' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                             
if any(word == 'city' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                     
if any(word == 'child' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'children' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()      
if any(word == 'crime' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                      
if any(word == 'cruelty' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                                    
if any(word == 'father' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                                                                                    
if any(word == 'government' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()                                                                                                                                                                                                       
if any(word == 'governor' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                                                                                                                                                                                                                                                                                                     
if any(word == 'language' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render() 
if any(word == 'mother' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                         
if any(word == 'people' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                                                                                                                
if any(word == 'passengers' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()  
if any(word == 'person' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()        
if any(word == 'personal' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                           
if any(word == 'population' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                                                                                                                                                                                                                                                                                                                         
if any(word == 'society' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
if any(word == 'struggle' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
if any(word == 'together' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
if any(word == 'war' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
if any(word == 'majority' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
if any(word == 'vote' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render() 
if any(word == 'pioneers' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
if any(word == 'consultant' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
if any(word == 'cure' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'medicinal' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'authority' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                        
if any(word == 'bandage' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'master' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                                                                                                                                                                                                                                                                                                                                                                                                                                                               
if any(word == 'classes' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()                                                                         
if any(word == 'luxury' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash      
    port.render()                                                                              
if any(word == 'miles' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash      
    port.render()                                                                                      
if any(word == 'approximate' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash       
    port.render()                                                                                              
if any(word == 'approximation' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'degrees' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()                                                                                                                                                                                                                                 
if any(word == 'favor' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()          


################################################################    
#life    
if any(word == 'rest' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'confessor' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'beauty' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'beauties' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()         
if any(word == 'divisiveness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'forgiveness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()                       
if any(word == 'freedom' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'grand' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render() 
if any(word == 'great' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'habit' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'happiness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'hatreds' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()         
if any(word == 'home' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'jealousy' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()                         
if any(word == 'me' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'misery' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()       
if any(word == 'necessity' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'one' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'pattern' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'peace' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()        
if any(word == 'please' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'predjudice' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                      
if any(word == 'prerogatives' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'responsibility' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render() 
if any(word == 'selfishness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'thinking' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'transients' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'truth' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()       
if any(word == 'violence' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'well-being' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash     
    port.render()                      
if any(word == 'idea' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render() 
if any(word == 'ideas' for word in keywords):
    port.dmx_frame[36] = 99 #UR wash      
    port.render()                                                            
if any(word == 'imaginary' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'imagination' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash      
    port.render()                                                                                                                                                                                                                                                                                                                                                            
################################################################
#senses        
if any(word == 'sight' for word in keywords):
    port.dmx_frame[26] = 255 #very DL spot (on lightboard)
    port.render()              
if any(word == 'recollection' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'ugly' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()       
if any(word == 'antiseptic' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'blast' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'cold' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'cool' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'cooler' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'fresh' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'germ-free' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'harmony' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'hear' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
if any(word == 'heat' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
if any(word == 'hungry' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'loud' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'music' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'noise' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'quiet' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'scared' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'sight' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'sing' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'smell' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'sound' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'sterile' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'sunny' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'temperature' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'thrist' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()       
if any(word == 'warm' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11)   
    port.render()
if any(word == 'weight' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'weightlessness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()       
if any(word == 'weights' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'refrigerated' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'darkness' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash   
    port.render()       
if any(word == 'decompression' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
if any(word == 'Gossamer' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render() 
################################################################  
#death 
if any(word == 'death' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash    
    port.render()      
if any(word == 'die' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render() 
if any(word == 'died' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()        
if any(word == 'grave' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash          
if any(word == 'alive' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
if any(word == 'live' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
if any(word == 'life' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
if any(word == 'living' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash                 
if any(word == 'exist' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
if any(word == 'suicide' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
if any(word == 'survival' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
if any(word == 'survive' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash          
if any(word == 'suffer' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
if any(word == 'suffered' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
if any(word == 'suffering' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash         
################################################################################################                    
#places                             
if any(word == 'door' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'direction' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render()   
if any(word == 'scene' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'here' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'place' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash 
    port.render()   
if any(word == 'someplace' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  
if any(word == 'paradise' for word in keywords):
    chans_sleep(23,34,1,35,7,18,2,11) #UR wash  
    port.render()  

    #port.blackout()
      
lights_sleep() 
print('blackout - or execute again')
    
##########################################################################################
##########################################################################################    


    

    
    
    


# immediate-mode commands, for drag-and-drop or execfile() execution
#if __name__ == '__main__':
#	if len(sys.argv) == 2:
#		run(sys.argv[1])		# accept a command-line filename
#	else:
#		run()
	#print
	#raw_input("press Return>")
#else:
#	print "Module shaney imported."
#	print "To run, type: shaney.run()"
#	print "To reload after changes to the source, type: reload(shaney)"

# end of shaney.py

##########################################################################################
##########################################################################################