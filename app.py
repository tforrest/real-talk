from flask import Flask
from flask_ask import Ask, session

from intents import get_current_intent

app = Flask(__name__)
ask = Ask(app, '/')


@ask.intent('RealTalk')
def real_talk(response):
    state = session.attributes.get('state', 0)
    if current_state == 0:
        session.attributes['data'] = {
            'sessionID': session.user.userID
        }
        state = 1
        session.attributes['state'] = state
    intent_fn = get_current_intent(state)
    return intent_fn()

if __name__ == '__main__':
    app.run(debug=True)