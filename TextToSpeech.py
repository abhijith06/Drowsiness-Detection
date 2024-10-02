# Import the required module for text
# to speech conversion
from gtts import gTTS
import playsound

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'take some fresh air sir'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("TakeSomeFreshAirSir.mp3")

# Playing the converted file
#os.system("mpg321 WakeUpSir.mp3")
playsound.playsound("C:/Users/Abhijith Shiva/PycharmProjects/drowsydriverr/TakeSomeFreshAirSir.mp3",True)