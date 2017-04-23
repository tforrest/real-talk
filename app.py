from flask import Flask
from flask_ask import Ask, session

from intents import _current_intent, logging

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('RealTalk')
def real_talk(response):
    state = session.attributes.get('state', 0)
    logging.critical(state)
    if state == 0:
        session.attributes['data'] = {
            'sessionID': session.user.userID
        }
        session.attributes['state'] = state
    return _current_intent(state, response)()

if __name__ == '__main__':
    app.run(debug=True)