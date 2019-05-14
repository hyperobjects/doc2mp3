In an increasingly visually dense world, where our eyes are constantly distracted, 
sometimes it’s easier to listen an article on the go than to sit and read. Now you can convert docx and pdf files to mp3s!

This simple python script is poses a solution to those who have too many articles to read, but, for whatever reason, their eyes are busy. 
Play and load converted docs as you would any other mp3 file. 

Current functionality only supports docx and pdf file types. 

To use this script, all you have to do is:

1. From terminal, execute: python doc2mp3.py 
2. Enter the name of the the docx or pdf text file when prompted to do so
3. Voilà! An message will appear saying the mp3 has been created file

Depending on document size, the mp3 may take a few minutes before it is playable.

NOTE: be sure to place doc2mp3.py in the same directory as the file that you want to convert to an mp3. 

Languages currently supported: 
 af: Afrikaans
  ar: Arabic
  bn: Bengali
  bs: Bosnian
  ca: Catalan
  cs: Czech
  cy: Welsh
  da: Danish
  de: German
  el: Greek
  en-us: English (US)
  eo: Esperanto
  es-us: Spanish (United States)
  es: Spanish
  et: Estonian
  fi: Finnish
  fr-fr: French (France)
  fr: French
  hi: Hindi
  hr: Croatian
  hu: Hungarian
  hy: Armenian
  id: Indonesian
  is: Icelandic
  it: Italian
  ja: Japanese
  jw: Javanese
  km: Khmer
  ko: Korean
  la: Latin
  lv: Latvian
  mk: Macedonian
  ml: Malayalam
  mr: Marathi
  my: Myanmar (Burmese)
  ne: Nepali
  nl: Dutch
  no: Norwegian
  pl: Polish
  pt-br: Portuguese (Brazil)
  pt: Portuguese
  ro: Romanian
  ru: Russian
  si: Sinhala
  sk: Slovak
  sq: Albanian
  sr: Serbian
  su: Sundanese
  sv: Swedish
  sw: Swahili
  ta: Tamil
  te: Telugu
  th: Thai
  tl: Filipino
  tr: Turkish
  uk: Ukrainian
  vi: Vietnamese
  zh-tw: Chinese (Mandarin/Taiwan)
  
Dependencies: 
pip install gTTS 
pip install python-docx
pip install pdftotext 
pip install cld2

pdftotext may have system specific dependencies, for more info check their readme: https://github.com/jalan/pdftotext/blob/master/README.md
