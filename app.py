from flask import Flask
from flask_ask import Ask, session, statement

from intents import _current_intent, logging

app = Flask(__name__)
ask = Ask(app, '/')


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
    state = session.attributes.get('state', None)
    logging.critical(state)
    if not state:
        session.attributes['data'] = {
            'sessionID': session.user.userID
        }
        state = 0
        session.attributes['state'] = state
        return _welcome_intent()
    return _current_intent(state, response)()

if __name__ == '__main__':
    app.run(debug=True)