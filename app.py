from flask import Flask
from flask_ask import Ask, statement, question, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('helloworld')
def hello(mood_level):
    speech_text = "Hello %s! This is working" % firstname
    return statement(speech_text).simple_card('Hello', speech_text)

if __name__ == '__main__':
    app.run(debug=True)