from gtts import gTTS
import os

# Text to be converted to speech
"""with open('text.txt', 'r') as file:
    text = file.read()"""

# Or ask the user for the text

text = input("Enter the text you want to convert to speech: ")

# Create a gTTS object
tts = gTTS(text)

# Save the generated speech as an audio file
tts.save("voiceNote.mp3")

# Play the generated voice note
os.system("start voiceNote.mp3")