# TAPS_BA_2018
"Beyond It Is Another Dimension" (2018) for the completion of Theater and Performance Studies Minor  

Created and Directed by Margaret Lazarovits  
B.A. Thesis     
Department of Theater and Performance Studies     
University of Chicago     
Preceptor: Leslie Buxbaum Danzig      
Spring 2018, Reva and David Logan Center for the Arts Room 701      



[Video recording of Beyond It Is Another Dimension with talkback](https://drive.google.com/file/d/1M5hGk0_FrW9PgXpwj9EQJLGV1RF6Xq8I/view?usp=sharing)

Python 3 necessary packages:  
numpy   
random  
Algorithmia - to generate keywords   
pyttsx3 - to do text to speech   
import pyenttec as dmx - for light cues   

To run: 
```
python shaney_play.py
```
This command will create a new script from the original one using a Markov chain to string together sentences from one chosen script (from `scriptChoices/`). The number of sentences generated is 10 but can be changed by changing the `count` parameter in the `run` function.
After the new script has been generated, the text-to-speech generator will say the new script out loud. Then, the light cues will begin. These light cues are trigged by keywords found in the new script.

Note: you must have an active DMX connection to a lightboard to view the light cues.

Special thanks to Yisong Yue's [website](http://www.yisongyue.com/shaney/) and python code for the Markov chain implementation.
