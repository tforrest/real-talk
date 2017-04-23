from flask import Flask
from flask_ask import Ask, session

from intents import _current_intent

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('RealTalk')
def real_talk(response):
    state = session.attributes.get('state', 0)
    if state == 0:
        session.attributes['data'] = {
            'sessionID': session.user.userID
        }
        state = 1
        session.attributes['state'] = state
    return _current_intent(state)()

if __name__ == '__main__':
    app.run(debug=True)