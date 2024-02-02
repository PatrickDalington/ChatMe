import pathlib
import textwrap

import google.generativeai as genai

import cv2

from IPython.display import display
from IPython.display import Markdown
import PIL.Image

GOOGLE_API_KEY = 'AIzaSyCZ9bcO143UYOhRTs1a9tXRJzXjpu5vtIM'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


# Taking image as input
# model = genai.GenerativeModel('gemini-pro')
# img = PIL.Image.open('musk.png')
#response = model.generate_content(img)


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


response = model.generate_content("What is the meaning of life?")
print(response.text)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
