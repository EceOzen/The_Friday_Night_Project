# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:40:17 2023

@author: Ece
"""
from gtts import gTTS
import PyPDF2

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_speech(text, output_path='output.mp3', language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save(output_path)

if __name__ == "__main__":
    text_content = pdf_to_text(path)
    if text_content:
        text_to_speech(text_content)
        print("Speech generated successfully.")
    else:
          print("Error: Unable to extract text from the PDF.")
