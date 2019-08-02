#!/usr/bin/python3

from docx import Document
import pdftotext 

fullText = []
fname = input(" Please enter the full file name you would like to convert to mp3.")

#detect doc type 
if fname.endswith('.docx'):
    document = Document(fname)
    for p in document.paragraphs:
        fullText.append(p.text)
    fullText = str(fullText)
    
elif fname.endswith('.pdf'):
    with open(fname, "rb") as pdf:
        pdf = pdftotext.PDF(pdf)
    fullText = "\n\n".join(pdf)
    fullText = fullText.replace('\n', '')
    fullText = str(fullText)
    
elif "." not in fname:
    raise Exception(" Please re-enter the full file name, including the extension.")
    
else: 
     raise Exception(" Sorry, the current version of this script only supports converting pdf and docx files to mp3s.")

#detect language
import cld2
details = cld2.detect(fullText)
x = str(details)
y =x.split("language_code='")
lang = y[1][:2]

if lang =="zh":
    lang="zh-tw" #Taiwanese Mandarin
if lang == "pt":
    lang=="pt-br" #Brazilian Portuguese
if lang =="fr":
    lang=="fr-fr" #French French
if lang == "en":  
    lang =="en-us" #US English
if lang == "es":
    lang == "es-us" #US Spanish

#turn into mp3 
from gtts import gTTS  #import google text to speech
tts = gTTS(text=fullText, lang=lang) 
#fn = input ('enter name of the mp3')
tts.save(fn[0]+".mp3")
print(fn[0]+".mp3 now created! You can find it in your local directory.")
