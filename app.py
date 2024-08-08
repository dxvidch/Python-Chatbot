from flask import Flask, request, render_template, redirect, url_for
from gemini import get_gemini_response

# Initialize the app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chat_history = []
    if request.method == 'POST':
        question = request.form['question']
        response = get_gemini_response(question)
        response_text = [chunk.text for chunk in response]
        chat_history.append(('You', question))
        for chunk in response_text:
            chat_history.append(('Bot', chunk))
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
