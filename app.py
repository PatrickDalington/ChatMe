from flask import Flask, request, render_template

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY = 'API_KEY'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

app = Flask(__name__)

questions = []
homeQuestions = []
answers = []

qAndA = [[]]


@app.route('/')
def home():

    return render_template('home.html', chat=chat.history)


@app.route('/add', methods=['GET', 'POST'])
def add():
    question = request.form['question']

    chat.send_message(question)
    response = model.generate_content(question)

    answers.append(response.text)
    questions.append(question)

    qa = zip(questions, answers)

    return render_template('home.html', response=response.text, qa=qa)


if __name__ == '__main__':
    app.run(debug=True)
