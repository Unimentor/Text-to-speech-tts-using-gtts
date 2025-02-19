from gtts import gTTS
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Function to extract text from EPUB
def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    text = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
            text.append(soup.get_text())
    return '\n'.join(text)

# Path to the EPUB file
epub_path = r'Path_to_epub_file.epub' #enter the path to the epub file you want to convert to audio

# Extract text from the EPUB file
text = extract_text_from_epub(epub_path)

# Create a gTTS object
tts = gTTS(text)

# Save the generated speech as an audio file
tts.save("name_of_the_file.mp3") #enter the name of the file you want to save the audio as
# Play the generated voice note
os.system("name_of_your_file.mp3")