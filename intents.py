from flask_ask import Ask, statement, question, convert_errors, request, session

def _general_intent(general_level, next_question, error_question, reprompt_question):
	try:
		general_level = int(general_level)
		if general_level < 1 or general_level > 5:
			raise ValueError("Attribute out of range")
	except ValueError as e:
		return lambda fn: question(error_question).reprompt(reprompt_question)
	return lambda fn: question(next_question).reprompt(next_question)

def mood_intent(mood_level):
	pass

def productivity_intent(productivity_level):
    pass

def sleep_intent(sleep_level):
    pass

def excercise_intent(answer):
    pass

def entertainment_intent(answer):
    pass

def schoolwork_intent(answer):
    pass

def work_intent(answer):
    pass

def socialize_intent(answer):
    pass

def conflict_intent(answer):
    pass