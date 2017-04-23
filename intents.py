import logging
import random

from flask_ask import Ask, statement, question, request, session

from settings import table

MOOD_QUESTION = 'On a scale from 1 to 5, how positive was your mood today?'
PRODUCTIVITY_QUESTION = 'On a scale from 1 to 5, how good was your productivity today?'
SLEEP_QUESTION = 'On a scale from 1 to 5, how well did you sleep?'
EXERCISE_QUESTION = 'Did you exercise today?'
ENTERTAINMENT_QUESTION = 'Did you consume any entertainment during the day?'
SCHOOLWORK_QUESTION = 'Was there any homework completed today?'
SOCIALIZE_QUESTION = 'Did you socialize with anyone today?'
CONFLICT_QUESTION = 'Did you get into a conflict with someone today?'

def _current_intent(state, response):
	logging.critical("%d state", state)
	if state == 0:
		curr_intent = mood_intent(response)
	elif state == 1:
		curr_intent = productivity_intent(response)
	elif state == 2:
		curr_intent = sleep_intent(response)
	elif state == 3:
		curr_intent = exercise_intent(response)
	elif state == 4:
		curr_intent = entertainment_intent(response)
	elif state == 5:
		curr_intent = schoolwork_intent(response)
	elif state == 6:
		curr_intent = socialize_intent(response)
	elif state == 7:
		curr_intent = conflict_intent(response)
	else:
		curr_intent = end_session_and_save
	return curr_intent

def end_session_and_save():
	try:
		data = session.attributes['data']
		data.update({
			'dayOfWeek': 'Monday',
			'sleepWell': True,
			'sessionID': "12313",
			'userID': "123123",
			'readingTS': '1:00'

		})
		table.put_item(Item=data)
	except Exception as e:
		logging.error(session.attributes['data'])
		logging.error(e)
	return statement("Your response have been saved!")

def _int_intent(general_level, next_question, error_question, reprompt_question, lower, upper, stat):
	try:
		general_level = int(general_level)
		if general_level < lower or general_level > upper:
			raise ValueError("Attribute out of range")
	except Exception as e:
		# lol 
		general_level = random.choice(range(1,6))
	session.attributes['state'] += 1
	session.attributes['data'][stat] = general_level
	return lambda: question(next_question).reprompt(next_question)

def _bool_intent(boolean_level, next_question, error_question, reprompt_question, stat):
	boolean = None
	if str(boolean_level).lower() == 'true':
		boolean = True
	elif str(boolean_level).lower() == 'false':
		boolean = False
	else:
		# lol
		boolean = random.choice([True, False])
	session.attributes['state'] += 1
	session.attributes['data'][stat] = boolean
	if session.attributes['state'] > 7:
		return end_session_and_save
	return lambda: question(next_question).reprompt(next_question)

def mood_intent(mood_level):
	return _int_intent(
		mood_level,
		PRODUCTIVITY_QUESTION,
		"From 1 to 5, how was your mood today?",
		MOOD_QUESTION,
		1,
		5,
		'mood'
	)

def productivity_intent(productivity_level):
	return _int_intent(
		productivity_level,
		SLEEP_QUESTION,
		"Please give a number between 1 and 5 for your productivity",
		PRODUCTIVITY_QUESTION,
		1,
		5,
		'productivity'
	)

def sleep_intent(sleep_level):
    return _int_intent(
		sleep_level,
		EXERCISE_QUESTION,
		"From 1 to 5, how well did you sleep today?",
		SLEEP_QUESTION,
		1,
		24,
		'sleepHrs'
	)

def exercise_intent(exercise_level):
    return _bool_intent(
		exercise_level,
		ENTERTAINMENT_QUESTION,
		"Did you exercise today?",
		EXERCISE_QUESTION,
		'exercise'
	)

def entertainment_intent(entertainment):
    return _bool_intent(
		entertainment,
		SCHOOLWORK_QUESTION,
		"Did you consume any entertainment?",
		ENTERTAINMENT_QUESTION,
		'entertainment'
	)

def schoolwork_intent(school):
    return _bool_intent(
		school,
		SOCIALIZE_QUESTION,
		"Was any school work done?",
		SCHOOLWORK_QUESTION,
		'schoolwork'

	)

def socialize_intent(socialize):
    return _bool_intent(
		socialize,
		CONFLICT_QUESTION,
		"Did you socialized with anyone today?",
		SOCIALIZE_QUESTION,
		'socialized'
	)

def conflict_intent(conflict):
    return _bool_intent(
		conflict,
		'DONE',
		"Did you get into a conflict with another student, friend, or family member today?",
		CONFLICT_QUESTION,
		'conflict'
	)