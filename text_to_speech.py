#sample code to text to speech using google translate
from gtts import gTTS
import os
  
# The text that you want to convert to audio
mytext = 'A sample text to speech'
  
# Language in which you want to convert
language = 'en'
#For indian accent
top_level = 'co.in'
  
#gtts object
myobj = gTTS(text=mytext, lang=language, tld=top_level, slow=True)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("welcome.mp3")