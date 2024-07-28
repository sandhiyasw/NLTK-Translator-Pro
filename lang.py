import streamlit as st
from mtranslate import translate  # Once the package is installed, you can use it to translate tex
import pandas as pd
import os
from gtts import gTTS
import base64  # Base64 encoding is a way to encode binary data into ASCII characters. It is commonly used for encoding data that needs to be stored and transferred over media that are designed to deal with text
'''# Translate a phrase from English to Spanish
translated_text = translate("Hello, how are you?", "es")
print(translated_text)'''

# read language dataset
df = pd.read_csv(r"C:\Users\sandh\OneDrive\Desktop\python\july22nd_pendingwork _multilanguague converter_frontendstreamlit\New folder\language.csv")
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist=tuple(lang)
langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# layout
st.title("Language-Translation")
inputtext = st.text_area("Hi Please Enter text here to Translate",height=100) # in front end user enter input text 

choice = st.sidebar.radio('SELECT LANGUAGE',langlist)

speech_langs = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jw": "Javanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "la": "Latin",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Filipino",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-CN": "Chinese"
}

# function to decode audio file for download
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href
'''Encoding Data:
Convert the string to bytes using encode('utf-8').
Encode the bytes using base64.b64encode().
Convert the encoded bytes back to a string using decode('utf-8').
Decoding Data:
Convert the Base64 encoded string to bytes using encode('utf-8')'''


c1,c2 = st.columns([4,3])    # Create two columns with relative widths 4 and 3

# I/O
if len(inputtext) > 0 :
    try:
        output = translate(inputtext,lang_array[choice])
        with c1:
            st.text_area("TRANSLATED TEXT",output,height=200)
        # if speech support is available will render audio file
        if choice in speech_langs.values():
            with c2:
                aud_file = gTTS(text=output, lang=lang_array[choice], slow=False)
                aud_file.save("lang.mp3")
                audio_file_read = open('lang.mp3', 'rb')
                audio_bytes = audio_file_read.read()
                bin_str = base64.b64encode(audio_bytes).decode()
                st.audio(audio_bytes, format='audio/mp3')
                st.markdown(get_binary_file_downloader_html("lang.mp3", 'Audio File'), unsafe_allow_html=True)
    except Exception as e:
        st.error(e)





    """Above script snippet is designed to translate input text, display the translated text, and provide an audio file for download if speech support is available.Explanation
Input Check: The script first checks if there is any input text provided.
Translation: It tries to translate the input text using the specified language from the lang_array dictionary based on the choice.
Display Translated Text: The translated text is displayed in a text area in column c1.
Text-to-Speech: If the chosen language supports speech, the script generates an audio file using gTTS (Google Text-to-Speech).
Display and Download Audio: The audio file is played in the app and a download link is provided."""
"""This script sets up a basic Streamlit app to translate text, display the translated text, generate speech, and provide a download link for the generated audio file. Adjust the language options and user input handling as needed for your specific use case."""