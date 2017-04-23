from flask import Flask
from flask_ask import Ask, session, statement, question

from intents import _current_intent, logging, MOOD_QUESTION

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.intent('AMAZON.HelpIntent')
def help():
    return statement('Real talk tracks your moods by asking you questions every day')

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement('Thanks for using Real Talk')

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement('Thanks for using Real Talk')

@ask.intent('RealTalk')
def real_talk(response):
    state = session.attributes.get('state', 0)
    logging.debug(state)
    if 'data' not in session.attributes:
        session.attributes['data'] = {}
        session.attributes['state'] = 0
        return question(MOOD_QUESTION)
    return _current_intent(state, response)()

if __name__ == '__main__':
    app.run(debug=True)