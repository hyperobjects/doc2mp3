In an increasingly visually dense world, where our eyes are constantly distracted, 
sometimes it’s easier to listen an article on the go than to sit and read. Now you can convert docx and pdf files to mp3s!

This simple python script is poses a solution to those who have too many articles to read, but, for whatever reason, their eyes are busy. 
Play and load converted docs as you would any other mp3 file. 

Current functionality only allows one to convert English language docx and pdf file types. 
I intend to add multilingual support and more file types soon.  

All you have to do is:

1. From terminal, execute: python doc2mp3.py 
2. Enter the name of the the docx or pdf text file when prompted to do so
3. Voilà! An mp3 will be created with the same name as the original file

Depending on document size, the mp3 may take a few minutes before it is playable.  

NOTE: be sure to place doc2mp3.py in the same directory as the file that you want to convert to an mp3. 


Dependencies: 
pip install gTTS 
pip install python-docx
pip install pdftotext 

pdftotext may have system specific dependencies, for more info check their readme: https://github.com/jalan/pdftotext/blob/master/README.md
